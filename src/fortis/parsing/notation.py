"""Recursive-descent parser for Fortis rule notation.

Consumes the token stream from :func:`src.fortis.parsing.lexer.lex` and produces
a ``StructuralDescription``, wrapped in a ``Result``. The parser owns the feature
inventory because the only place it is needed is when a ``Token.BUNDLE`` is
reduced into a bundle: pattern-side brackets become a ``BundleElem`` (via
``parse_pattern_bundle``) and result-side brackets a ``ResultElem`` (via
``parse_result_bundle``). The side is threaded as the bundle parser itself, so a
group or disjunction inherits whichever side it sits in without a separate flag.

Error handling collects what can be collected. A failed bundle does not desync
the token stream (the bracket is one opaque token), so its messages are recorded,
a placeholder is dropped in its slot, and parsing continues -- a rule with
several bad bundles reports them all. A structural failure (a missing arrow,
unbalanced parens, a malformed count) desyncs a recursive-descent parser, so it
is recorded and parsing stops. ``parse_definition`` never raises: a ``LexError``
is returned as a one-item ``Err`` as well.

The grammar::

    definition  := target ARROW result (SLASH context)? (SLASH SLASH exception)?
    context     := environment
    exception   := environment
    environment := sequence FOCUS sequence
    sequence    := element*
    element     := (INT EQ)? unit                            # Bound
    unit        := BANG? atom quantifier?
    atom        := BUNDLE | null | recall | NAME | group | BOUNDARY | FLOATING
    recall      := AT INT                                    # RecallRef
    null        := "∅" | "0"
    group       := LPAREN sequence (PIPE sequence)* RPAREN   # 1 alt -> Group, >1 -> Disjunction
    quantifier  := STAR | PLUS | QMARK | count
    count       := LBRACE int? (COMMA int?)? RBRACE          # missing min -> 0; bare {} rejected

A leading ``!`` negates the whole following atom; a trailing quantifier wraps the
negation, so ``!X+`` is "one or more non-X". A binding prefix ``1=`` wraps the
whole unit, so ``1=![nas]+`` is ``Bound(1, Quantified(Negated(...), ...))``. The
element-level ``!`` is distinct from the spec- and value-level ``!`` handled
inside ``[ ... ]`` by the bundle parser; the two never meet because the lexer
treats a bracket as opaque.

Bracketing is a clean partition: ``[ ]`` is an opaque bundle (or ``[]`` a
``Wildcard``), ``{ }`` is always a count, ``( )`` is always a group or
disjunction, ``|`` is meaningful only inside ``( )``, and ``,`` only inside
``{ }``. Context is introduced by ``/`` and the exception by ``//``.

The parser is permissive about linguistic legality: a wildcard in result
position, a back-reference index of 0, an empty alternation, and so on are
representable and left for the validation pass.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import NoReturn

from src.fortis.models.elements import (
    Bound,
    BundleElem,
    Disjunction,
    Element,
    FloatingAutoseg,
    Group,
    LetterRef,
    ModifiedLetter,
    Negated,
    Null,
    Quantified,
    Quantifier,
    RecallRef,
    ResultElem,
    SyllableBoundary,
    Wildcard,
    WordBoundary,
)
from src.fortis.models.features import FeatureInventory
from src.fortis.models.rules import StructuralDescription
from src.fortis.parsing.bundles import (
    parse_feature_bundle,
    parse_pattern_bundle,
    parse_result_bundle,
)
from src.fortis.parsing.lexer import LexError, Token, TokenInfo, lex
from src.fortis.result import Err, Ok, Result

__all__ = ["parse_definition"]

# Simple postfix quantifiers and their (minimum, maximum) bounds. The counted
# form `{n,m}` is handled separately because it spans more than one token.
_QUANT_BOUNDS: dict[Token, tuple[int, int | None]] = {
    Token.STAR: (0, None),
    Token.PLUS: (1, None),
    Token.QMARK: (0, 1),
}

# Symbols that denote the null segment. Could be sourced from config's special
# symbols if a single source of truth is wanted.
_NULL_SYMBOLS: frozenset[str] = frozenset({"∅", "0"})

# A callable that reduces a `[ ... ]` bundle token into an Element.
BundleParser = Callable[[TokenInfo], Element]


class _Abort(Exception):
    """Internal signal: a structural failure parsing cannot recover from."""


def parse_definition(
    source: str, features: FeatureInventory
) -> Result[StructuralDescription, list[str]]:
    """Parse a rule-notation string into a structural description.

    Args:
        source: The notation, e.g. ``"1=![nas] → [+voice] / V _ @1 // _ #"``.
        features: The feature inventory, needed to parse embedded bundles.

    Returns:
        ``Ok`` with the structural description, or ``Err`` with every collected
        error message. Bundle errors are gathered across the whole rule; a
        structural error is the last one collected.
    """
    return _Parser(source, features).parse()


def parse_sequence(
    source: str, features: FeatureInventory
) -> Result[tuple[Element, ...], list[str]]:
    """Parse a bare element sequence (no ``->``/context), e.g. an onset/coda pattern.

    Args:
        source: The notation, e.g. ``"[+cons][-syll, -cons]?"``.
        features: The feature inventory, needed to parse embedded bundles.

    Returns:
        ``Ok`` with the element tuple, or ``Err`` with every collected error.
    """
    return _Parser(source, features).parse_sequence()


class _Parser:
    """A single-use cursor over the token stream.

    Args:
        source: The notation source, retained for error positions.
        features: The feature inventory, closed over by the bundle parsers.
    """

    def __init__(self, source: str, features: FeatureInventory) -> None:
        self._source = source
        self._features = features
        self._toks: list[TokenInfo] = []
        self._i = 0
        self._errors: list[str] = []

    # -- entry point ------------------------------------------------------- #

    def parse(self) -> Result[StructuralDescription, list[str]]:
        """Lex and parse, returning the description or all collected errors."""
        try:
            self._toks = lex(self._source)
        except LexError as exc:
            return Err([self._format(exc.message, exc.pos)])

        try:
            sd = self._definition()
        except _Abort:
            return Err(self._errors)

        if self._errors:
            return Err(self._errors)
        return Ok(sd)

    def parse_sequence(self) -> Result[tuple[Element, ...], list[str]]:
        """Lex and parse a bare pattern sequence to end of input."""
        try:
            self._toks = lex(self._source)
        except LexError as exc:
            return Err([self._format(exc.message, exc.pos)])

        try:
            sequence = self._sequence(frozenset(), self._pattern_bundle)
            self._expect_end()
        except _Abort:
            return Err(self._errors)

        if self._errors:
            return Err(self._errors)
        return Ok(sequence)

    def _definition(self) -> StructuralDescription:
        """Parse the full ``definition`` production."""
        target = self._sequence({Token.ARROW, Token.SLASH}, self._pattern_bundle)
        self._expect(Token.ARROW)
        result = self._sequence({Token.SLASH}, self._result_bundle)

        left_context: tuple[Element, ...] = ()
        right_context: tuple[Element, ...] = ()
        left_exception: tuple[Element, ...] = ()
        right_exception: tuple[Element, ...] = ()

        # Context is a single '/'; the exception is '//'. A '/' that is the
        # first half of a '//' is left for the exception clause.
        if self._at(Token.SLASH) and not self._at_double_slash():
            self._advance()
            left_context, right_context = self._environment({Token.SLASH})

        if self._at(Token.SLASH):
            self._expect(Token.SLASH)
            self._expect(Token.SLASH)
            left_exception, right_exception = self._environment(frozenset())

        self._expect_end()
        return StructuralDescription(
            target=target,
            result=result,
            left_context=left_context,
            right_context=right_context,
            left_exception=left_exception,
            right_exception=right_exception,
        )

    # -- productions ------------------------------------------------------- #

    def _environment(
        self, right_terminator: frozenset[Token] | set[Token]
    ) -> tuple[tuple[Element, ...], tuple[Element, ...]]:
        """Parse ``sequence FOCUS sequence``.

        Args:
            right_terminator: Terminators for the post-focus sequence -- the
                context stops at the exception's ``/``; the exception runs to
                end of input.
        """
        left = self._sequence({Token.FOCUS}, self._pattern_bundle)
        self._expect(Token.FOCUS)
        right = self._sequence(right_terminator, self._pattern_bundle)
        return left, right

    def _sequence(
        self, terminators: frozenset[Token] | set[Token], bundle: BundleParser
    ) -> tuple[Element, ...]:
        """Parse zero or more elements until a terminator or end of input.

        Args:
            terminators: Token kinds that end the sequence (not consumed).
            bundle: The bundle parser for this side (pattern or result).
        """
        elements: list[Element] = []
        while True:
            tok = self._peek()
            if tok is None or tok.kind in terminators:
                break
            elements.append(self._element(bundle))
        return tuple(elements)

    def _element(self, bundle: BundleParser) -> Element:
        """Parse an optional ``INT =`` binding prefix, then a unit."""
        if self._at_binding():
            ref = self._integer()
            self._expect(Token.EQ)
            return Bound(ref, self._unit(bundle))
        return self._unit(bundle)

    def _unit(self, bundle: BundleParser) -> Element:
        """Parse an optional ``!``, an ``atom``, and an optional quantifier."""
        negated = self._accept(Token.BANG)
        atom = self._atom(bundle)
        if negated:
            atom = Negated(atom)

        tok = self._peek()
        if tok is None:
            return atom
        if tok.kind in _QUANT_BOUNDS:
            self._advance()
            minimum, maximum = _QUANT_BOUNDS[tok.kind]
            return Quantified(atom, Quantifier(minimum, maximum))
        if tok.kind is Token.LBRACE:
            minimum, maximum = self._count()
            return Quantified(atom, Quantifier(minimum, maximum))
        return atom

    def _atom(self, bundle: BundleParser) -> Element:
        """Parse one atom: bundle, wildcard, null, recall, name, boundary, group, or floating."""
        tok = self._peek()
        if tok is None:
            self._fail("expected an element, found end of input")

        match tok.kind:
            case Token.BUNDLE:
                self._advance()
                if tok.text.strip() == "":
                    return Wildcard()
                return bundle(tok)
            case Token.FLOATING:
                self._advance()
                return self._floating(tok)
            case Token.AT:
                self._advance()
                return RecallRef(self._integer())
            case Token.NAME:
                self._advance()
                if tok.text in _NULL_SYMBOLS:
                    return Null()
                if self._accept(Token.CARET):
                    return self._modified_letter(tok)
                return LetterRef(tok.text)
            case Token.BOUNDARY:
                self._advance()
                return WordBoundary() if tok.text == "#" else SyllableBoundary()
            case Token.LPAREN:
                return self._paren(bundle)
            case _:
                self._fail(f"unexpected {tok.kind.name}", tok)

    def _paren(self, bundle: BundleParser) -> Element:
        """Parse ``( ... )``: a group, or a disjunction if it contains ``|``.

        One alternative yields a ``Group`` (so a following quantifier binds the
        whole subsequence); two or more yield a ``Disjunction``.
        """
        self._expect(Token.LPAREN)
        branches: list[tuple[Element, ...]] = [self._sequence({Token.PIPE, Token.RPAREN}, bundle)]
        while self._accept(Token.PIPE):
            branches.append(self._sequence({Token.PIPE, Token.RPAREN}, bundle))
        self._expect(Token.RPAREN)
        if len(branches) == 1:
            return Group(branches[0])
        return Disjunction(tuple(branches))

    def _count(self) -> tuple[int, int | None]:
        """Parse a counted quantifier: ``{n}``, ``{n,m}``, ``{n,}``, ``{,m}``.

        The minimum defaults to 0 when omitted, so ``{,m}`` is "zero to m" and
        ``{,}`` is unbounded. A bare ``{}`` expresses no bound and is rejected.
        """
        open_brace = self._expect(Token.LBRACE)
        has_min = self._at(Token.NAME)
        minimum = self._integer() if has_min else 0

        if self._accept(Token.COMMA):
            maximum: int | None = self._integer() if self._at(Token.NAME) else None
        elif has_min:
            maximum = minimum
        else:
            self._fail("empty count", open_brace)

        self._expect(Token.RBRACE)
        return minimum, maximum

    def _integer(self) -> int:
        """Consume a NAME token and read it as an integer."""
        tok = self._expect(Token.NAME)
        try:
            return int(tok.text)
        except ValueError:
            self._fail(f"expected an integer, found {tok.text!r}", tok)

    # -- bundle sides ------------------------------------------------------ #

    def _pattern_bundle(self, tok: TokenInfo) -> Element:
        """Reduce a pattern-side ``[ ... ]`` into a ``BundleElem``."""
        match parse_pattern_bundle(tok.text, self._features):
            case Ok(bundle):
                return BundleElem(bundle)
            case Err(errors):
                self._record(errors, tok)
                return Wildcard()  # placeholder; the Err path discards the tree

    def _floating(self, tok: TokenInfo) -> Element:
        """Reduce ``⟨ ... ⟩`` into a ``FloatingAutoseg`` (its inner is a pattern bundle)."""
        match parse_pattern_bundle(tok.text, self._features):
            case Ok(bundle):
                return FloatingAutoseg(bundle)
            case Err(errors):
                self._record(errors, tok)
                return Wildcard()

    def _modified_letter(self, name_tok: TokenInfo) -> Element:
        """Parse ``letter ^ [ Δ ]`` — a letter modified by a concrete feature bundle.

        Δ is parsed as a *realized* bundle (concrete values, including ``none``), so a
        negation/alpha/conditional inside is rejected here rather than silently mis-applied.
        """
        tok = self._expect(Token.BUNDLE)
        match parse_feature_bundle(tok.text, self._features):
            case Ok(delta):
                return ModifiedLetter(name_tok.text, delta)
            case Err(errors):
                self._record(errors, tok)
                return Wildcard()  # placeholder; the Err path discards the tree

    def _result_bundle(self, tok: TokenInfo) -> Element:
        """Reduce a result-side ``[ ... ]`` into a ``ResultElem``."""
        match parse_result_bundle(tok.text, self._features):
            case Ok(bundle):
                return ResultElem(bundle)
            case Err(errors):
                self._record(errors, tok)
                return Wildcard()  # placeholder; the Err path discards the tree

    # -- cursor ------------------------------------------------------------ #

    def _peek(self) -> TokenInfo | None:
        """Return the current token, or ``None`` at end of input."""
        return self._toks[self._i] if self._i < len(self._toks) else None

    def _at(self, kind: Token) -> bool:
        """Report whether the current token has ``kind`` (without consuming)."""
        tok = self._peek()
        return tok is not None and tok.kind is kind

    def _at_binding(self) -> bool:
        """Report whether the cursor sits at an ``INT =`` binding prefix."""
        tok = self._peek()
        if tok is None or tok.kind is not Token.NAME or not tok.text.isdigit():
            return False
        nxt = self._i + 1
        return nxt < len(self._toks) and self._toks[nxt].kind is Token.EQ

    def _at_double_slash(self) -> bool:
        """Report whether the cursor sits at a ``//`` exception marker."""
        return (
            self._at(Token.SLASH)
            and self._i + 1 < len(self._toks)
            and self._toks[self._i + 1].kind is Token.SLASH
        )

    def _advance(self) -> TokenInfo:
        """Consume and return the current token."""
        tok = self._toks[self._i]
        self._i += 1
        return tok

    def _accept(self, kind: Token) -> bool:
        """Consume the current token if it has ``kind``; report whether it did."""
        if self._at(kind):
            self._advance()
            return True
        return False

    def _expect(self, kind: Token) -> TokenInfo:
        """Consume the current token, requiring it to have ``kind``."""
        tok = self._peek()
        if tok is None or tok.kind is not kind:
            found = "end of input" if tok is None else tok.kind.name
            self._fail(f"expected {kind.name}, found {found}", tok)
        return self._advance()

    def _expect_end(self) -> None:
        """Require that no tokens remain."""
        tok = self._peek()
        if tok is not None:
            self._fail(f"unexpected trailing {tok.kind.name}", tok)

    # -- error accumulation ------------------------------------------------ #

    def _record(self, messages: list[str], tok: TokenInfo) -> None:
        """Record recoverable errors (a failed bundle) without aborting."""
        for message in messages:
            self._errors.append(self._format(message, tok.pos))

    def _fail(self, message: str, tok: TokenInfo | None = None) -> NoReturn:
        """Record an unrecoverable structural error and abort the parse."""
        pos = tok.pos if tok is not None else len(self._source)
        self._errors.append(self._format(message, pos))
        raise _Abort

    def _format(self, message: str, pos: int) -> str:
        """Render an error message with its source position."""
        return f"{message} at position {pos}"
