"""Lexer for Fortis rule notation.

Turns a rule-notation string into a flat list of :class:`TokenInfo`. The lexer
is deliberately *vocabulary-free*: it knows the structure of the notation
(arrows, slashes, brackets, grouping, quantifiers) but nothing about which
letters or features exist. Feature bundles are emitted whole as a single
``Token.BUNDLE`` carrying their raw inner text, so the recursive-descent parser
-- which owns the feature inventory -- can apply ``parse_pattern_bundle`` to
them later. This is also what keeps the bundle-internal ``>`` limb separator
from colliding with notation-level punctuation: the lexer never looks inside
``[ ... ]``.

A ``NAME`` is defined negatively: a maximal run of characters that are neither
whitespace nor structural punctuation. The lexer therefore accepts any IPA
letter name without consulting the inventory; whether the name refers to a real
letter is a question for validation, not lexing.
"""

from dataclasses import dataclass
from enum import Enum, auto

__all__ = ["Token", "TokenInfo", "LexError", "lex"]


class Token(Enum):
    """Kinds of lexical token in rule notation."""

    ARROW = auto()  # → or ->
    SLASH = auto()  # /
    FOCUS = auto()  # _
    LPAREN = auto()  # (
    RPAREN = auto()  # )
    LBRACE = auto()  # {
    RBRACE = auto()  # }
    COMMA = auto()  # ,
    STAR = auto()  # *
    PLUS = auto()  # +
    QMARK = auto()  # ?
    PIPE = auto()  # |   disjunction separator, only meaningful inside ( )
    BANG = auto()  # !   negates the following element
    EQ = auto()  # =   binds the following element to an index
    AT = auto()  # @   recalls a bound element by index
    BUNDLE = auto()  # [ ... ]  (text = inner, brackets stripped)
    BOUNDARY = auto()  # # or $   (text = the symbol)
    NAME = auto()  # a letter reference


@dataclass(frozen=True)
class TokenInfo:
    """A single lexed token.

    Attributes:
        kind: The token category.
        text: The matched source text. For ``Token.BUNDLE`` this is the inner
            text between the brackets with the brackets stripped (whitespace is
            left intact for the bundle parser to handle). For ``Token.BOUNDARY``
            it is the boundary symbol. For ``Token.NAME`` it is the name run.
        pos: Zero-based offset of the token's start in the source string, used
            for error reporting.
    """

    kind: Token
    text: str
    pos: int


class LexError(ValueError):
    """Raised when the notation string cannot be tokenized.

    Attributes:
        message: Human-readable description of the problem.
        source: The full source string being lexed.
        pos: Zero-based offset where the problem was detected.
    """

    def __init__(self, message: str, source: str, pos: int) -> None:
        """Initialize the class."""
        self.message = message
        self.source = source
        self.pos = pos
        super().__init__(f"{message} at position {pos}: {source!r}")


# --- Structural alphabet --------------------------------------------------- #
# These mirror the special symbols and could be sourced from ``config`` if a
# single source of truth is wanted; they are inlined here so the lexer has no
# cross-layer import.

_SINGLE: dict[str, Token] = {
    "/": Token.SLASH,
    "_": Token.FOCUS,
    "(": Token.LPAREN,
    ")": Token.RPAREN,
    "{": Token.LBRACE,
    "}": Token.RBRACE,
    ",": Token.COMMA,
    "*": Token.STAR,
    "+": Token.PLUS,
    "?": Token.QMARK,
    "|": Token.PIPE,
    "!": Token.BANG,
    "=": Token.EQ,
    "@": Token.AT,
}

_BOUNDARY: frozenset[str] = frozenset("#$")
_ARROW_HEAD: str = "→"  # single-character arrow; ``->`` is also accepted
_BRACKET_OPEN: str = "["
_BRACKET_CLOSE: str = "]"

# Characters that cannot appear inside a NAME run. Whitespace is tested
# separately via ``str.isspace`` so the lexer stays Unicode-correct.
_STOP: frozenset[str] = (
    frozenset(_SINGLE) | _BOUNDARY | frozenset({_BRACKET_OPEN, _BRACKET_CLOSE, _ARROW_HEAD, "-"})
)


def _is_stop(ch: str) -> bool:
    """Return whether ``ch`` terminates a NAME run."""
    return ch.isspace() or ch in _STOP


def lex(source: str) -> list[TokenInfo]:
    """Tokenize a rule-notation string.

    Args:
        source: The notation string, e.g. ``"[+nasal] → [+voice] / V _ V"``.

    Returns:
        The tokens in source order. Whitespace is consumed and not emitted.

    Raises:
        LexError: On an unterminated or stray bracket, a lone ``-`` that is not
            part of an arrow, or any other character that cannot start a token.
    """
    tokens: list[TokenInfo] = []
    i = 0
    n = len(source)

    while i < n:
        ch = source[i]

        if ch.isspace():
            i += 1
            continue

        if ch == _ARROW_HEAD:
            tokens.append(TokenInfo(Token.ARROW, ch, i))
            i += 1
            continue

        if ch == "-":
            if i + 1 < n and source[i + 1] == ">":
                tokens.append(TokenInfo(Token.ARROW, "->", i))
                i += 2
                continue
            raise LexError("expected '->' arrow after '-'", source, i)

        if ch == _BRACKET_OPEN:
            close = source.find(_BRACKET_CLOSE, i + 1)
            if close == -1:
                raise LexError("unterminated feature bundle", source, i)
            tokens.append(TokenInfo(Token.BUNDLE, source[i + 1 : close], i))
            i = close + 1
            continue

        if ch == _BRACKET_CLOSE:
            raise LexError("']' with no matching '['", source, i)

        if ch in _BOUNDARY:
            tokens.append(TokenInfo(Token.BOUNDARY, ch, i))
            i += 1
            continue

        single = _SINGLE.get(ch)
        if single is not None:
            tokens.append(TokenInfo(single, ch, i))
            i += 1
            continue

        # Otherwise: a NAME run -- a maximal span of non-structural characters.
        start = i
        while i < n and not _is_stop(source[i]):
            i += 1
        tokens.append(TokenInfo(Token.NAME, source[start:i], start))

    return tokens
