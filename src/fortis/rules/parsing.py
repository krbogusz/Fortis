"""Stage 1 — Parse a rule definition string into a Rule AST.

The parser converts a definition string like::

    [+cons, -syll] → [-vc] / _#

into a Rule object whose target, result, and context fields are lists of
Element nodes.  This is the only stage that can produce Err; downstream
stages (match, locus-finding, rewrite) operate on validated Rules.

Currently supported:
- Feature bundles in brackets: [+cons, -syll], [height:2], [hgt: high]
- Feature-level negation in bundles: [+cons, !nasal]
- Quantifiers: * (zero or more), + (one or more), {n}, {n,}, {n,m}
- Bundle-level negation: ![+cons] matches segments that do NOT satisfy the bundle
- Null segment: ∅ (U+2205) or 0 for insertion/deletion
- Groups: (...) with optional quantifiers, e.g. ([+cons][+nas])+
- Disjunction: | between element lists, e.g. [+cons]|[+nas]
- Binding: V=[+cons] captures a matched span as reference V
- Reference: @V recalls a previously saved span
- Arrows: → (Unicode) or -> (ASCII)
- Context clause with ``_`` position marker
- Word boundary ``#``
- Multi-segment contexts: [+nas][+cons]_
- Exception clause ``//``

Deferred to later phases:
- Alpha variables (``[α F]``), conditional features (``[<n: +F>]``)
- Syllable boundary (``$``), autosegmental notation (``===>``, ``=x=>``)
- Letter shorthands (``p``)
"""

from __future__ import annotations

import re

from src.fortis.inventories.feature_inventory import FeatureInventory
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.result import Err, Ok, Result
from src.fortis.rules.elements import Application, Binding, Boundary, Bundle, Disjunction, Element, Group, Null, Quantifier, Ref, _ONE
from src.fortis.rules.rule import Rule

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

type RuleParseResult = tuple[
    list[Element],  # target
    list[Element],  # result
    list[Element] | None,  # left_context
    list[Element] | None,  # right_context
    list[Element] | None,  # exception_left
    list[Element] | None,  # exception_right
]


def parse_rule_definition(
    definition: str,
    inventory: FeatureInventory,
    rule_id: str = "",
    name: str = "",
    description: str = "",
    time: int = 0,
    application: Application = Application.simultaneous,
) -> Result[Rule, list[str]]:
    """Parse a full rule definition string into a Rule object.

    Args:
        definition: The rule definition in SPE notation.
        inventory: Feature inventory for bundle parsing.
        rule_id: Rule identifier (from TOML key).
        name: Human-readable rule name.
        description: Rule description.
        time: Application time (lower = earlier).
        application: How the rule's matches are applied (simultaneous, left-to-right, right-to-left).

    Returns:
        Ok(Rule) on success, Err(list[str]) with accumulated errors on failure.
    """
    result = parse_spe_definition(definition, inventory)
    if result.is_err():
        return Err(result.unwrap_err())

    target, result_elems, left_ctx, right_ctx, exc_left, exc_right = result.unwrap()

    return Ok(
        Rule(
            rule_id=rule_id,
            name=name,
            time=time,
            description=description,
            target=target,
            result=result_elems,
            left_context=left_ctx,
            right_context=right_ctx,
            exception_left=exc_left,
            exception_right=exc_right,
            application=application,
        )
    )


def parse_spe_definition(definition: str, inventory: FeatureInventory) -> Result[RuleParseResult, list[str]]:
    """Parse an SPE-style rule definition string into Element lists.

    General form: ``A → B / C_D // E_F``

    Phase 1 supports feature bundles, arrows, context with ``_`` and ``#``,
    and exception clause parsing (stored but not yet applied).

    Args:
        definition: The rule definition string.
        inventory: Feature inventory for feature-bundle parsing.

    Returns:
        Ok(tuple) with (target, result, left_ctx, right_ctx, exc_left, exc_right),
        or Err(list[str]) with accumulated errors.
    """
    errors: list[str] = []
    definition = definition.strip()

    # ------------------------------------------------------------------
    # 1. Split on exception clause (//) — phase 1 parses but stores it
    # ------------------------------------------------------------------
    exception_part: str | None = None
    main_part = definition
    if "//" in definition:
        parts = definition.split("//", maxsplit=1)
        main_part = parts[0].strip()
        exception_part = parts[1].strip()

    # ------------------------------------------------------------------
    # 2. Split on arrow (→ or ->)
    # ------------------------------------------------------------------
    arrow_pos = _find_arrow(main_part)
    if arrow_pos is None:
        errors.append("Rule definition must contain '→' or '->'")
        return Err(errors)

    input_part = main_part[: arrow_pos[0]].strip()
    rest = main_part[arrow_pos[1] :].strip()

    # ------------------------------------------------------------------
    # 3. Split output + context on /
    # ------------------------------------------------------------------
    slash_pos = _find_unbracketed_slash(rest)
    if slash_pos is not None:
        output_part = rest[:slash_pos].strip()
        context_part = rest[slash_pos + 1 :].strip()
    else:
        output_part = rest
        context_part = None

    # ------------------------------------------------------------------
    # 4. Parse target and result as Element lists
    # ------------------------------------------------------------------
    target_result = _parse_element_list(input_part, inventory, "target")
    if target_result.is_err():
        errors.extend(target_result.unwrap_err())
        target_elems: list[Element] = []
    else:
        target_elems = target_result.unwrap()

    result_result = _parse_element_list(output_part, inventory, "result")
    if result_result.is_err():
        errors.extend(result_result.unwrap_err())
        result_elems: list[Element] = []
    else:
        result_elems = result_result.unwrap()

    # ------------------------------------------------------------------
    # 5. Parse context
    # ------------------------------------------------------------------
    left_ctx: list[Element] | None = None
    right_ctx: list[Element] | None = None
    if context_part is not None:
        ctx_result = _parse_context(context_part, inventory)
        if ctx_result.is_err():
            errors.extend(ctx_result.unwrap_err())
        else:
            left_ctx, right_ctx = ctx_result.unwrap()

    # ------------------------------------------------------------------
    # 6. Parse exception (phase 1: store only)
    # ------------------------------------------------------------------
    exc_left: list[Element] | None = None
    exc_right: list[Element] | None = None
    if exception_part is not None:
        exc_result = _parse_context(exception_part, inventory)
        if exc_result.is_err():
            errors.extend(exc_result.unwrap_err())
        else:
            exc_left, exc_right = exc_result.unwrap()

    if errors:
        return Err(errors)

    return Ok((target_elems, result_elems, left_ctx, right_ctx, exc_left, exc_right))


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

# Unicode arrow or ASCII ->
_ARROW_RE = re.compile(r"→|->")


def _find_arrow(s: str) -> tuple[int, int] | None:
    """Find the first arrow (→ or ->) outside brackets and parentheses.

    Returns (start, end) indices, or None if no arrow found.
    """
    depth = 0
    i = 0
    while i < len(s):
        if s[i] in ("[", "("):
            depth += 1
        elif s[i] in ("]", ")"):
            depth -= 1
        elif depth == 0:
            m = _ARROW_RE.match(s, i)
            if m:
                return (m.start(), m.end())
        i += 1
    return None


def _find_unbracketed_slash(s: str) -> int | None:
    """Find the first '/' outside brackets and parentheses.  Returns index or None."""
    depth = 0
    for i, ch in enumerate(s):
        if ch in ("[", "("):
            depth += 1
        elif ch in ("]", ")"):
            depth -= 1
        elif ch == "/" and depth == 0:
            return i
    return None


def _parse_quantifier(text: str, i: int) -> tuple[Quantifier, int]:
    """Parse a quantifier suffix starting at position *i*.

    Supports: ``*`` (0+), ``+`` (1+), ``{n}`` (exactly n), ``{n,}`` (n+),
    ``{n,m}`` (n to m).  Returns (Quantifier, next_position).  If no quantifier
    is found, returns (_ONE, i) unchanged.
    """
    if i >= len(text):
        return (_ONE, i)

    ch = text[i]

    if ch == "*":
        return (Quantifier(min=0, max=None), i + 1)
    if ch == "+":
        return (Quantifier(min=1, max=None), i + 1)
    if ch == "{":
        # Find closing brace
        end = text.find("}", i)
        if end == -1:
            return (_ONE, i)
        inner = text[i + 1 : end].strip()
        # {n} or {n,} or {n,m}
        if "," in inner:
            parts = inner.split(",", 1)
            try:
                n = int(parts[0].strip())
            except ValueError:
                return (_ONE, i)
            rest = parts[1].strip()
            if rest == "":
                return (Quantifier(min=n, max=None), end + 1)
            try:
                m = int(rest)
            except ValueError:
                return (_ONE, i)
            return (Quantifier(min=n, max=m), end + 1)
        else:
            try:
                n = int(inner)
            except ValueError:
                return (_ONE, i)
            return (Quantifier(min=n, max=n), end + 1)

    return (_ONE, i)


def _find_matching_bracket(text: str, start: int, open_ch: str = "(", close_ch: str = ")") -> int:
    """Find the matching closing bracket, respecting nesting.

    Args:
        text: The string to search.
        start: Index of the opening bracket.
        open_ch: Opening bracket character.
        close_ch: Closing bracket character.

    Returns:
        Index of the matching closing bracket, or -1 if unmatched.
    """
    depth = 0
    for i in range(start, len(text)):
        if text[i] == open_ch:
            depth += 1
        elif text[i] == close_ch:
            depth -= 1
            if depth == 0:
                return i
    return -1


def _split_on_pipe(text: str) -> list[str]:
    """Split text on ``|`` at depth 0 (outside brackets and parentheses).

    Returns a list of branch strings.  If no pipes are found, returns
    ``[text]``.
    """
    parts: list[str] = []
    depth = 0
    current_start = 0

    for i, ch in enumerate(text):
        if ch in ("[", "("):
            depth += 1
        elif ch in ("]", ")"):
            depth -= 1
        elif ch == "|" and depth == 0:
            parts.append(text[current_start:i].strip())
            current_start = i + 1

    parts.append(text[current_start:].strip())
    return [p for p in parts if p]


def _parse_element_list(text: str, inventory: FeatureInventory, label: str) -> Result[list[Element], list[str]]:
    """Parse a target or result string into a list of Elements.

    Supports:
    - Feature bundles in brackets: [+cons, -syll]
    - Quantifiers: [+cons]*, [+cons]+, [+cons]{2}, [+cons]{2,4}
    - Negation: ![+cons] (bundle-level), [+cons, !nasal] (feature-level)
    - Null segment: ∅ (U+2205) or 0
    - Groups: (...) with optional quantifiers
    - Disjunction: element | element (splits into branches)
    - Word boundaries: #
    - Syllable boundaries: $
    - Whitespace is ignored between elements
    """
    text = text.strip()

    if not text:
        return Err([f"Empty {label} in rule definition"])

    # Check for disjunction (|) at depth 0
    branches = _split_on_pipe(text)
    if len(branches) > 1:
        # Parse each branch as a separate element list
        all_branches: list[list[Element]] = []
        branch_errors: list[str] = []
        for branch_text in branches:
            branch_result = _parse_element_list(branch_text, inventory, f"{label} branch")
            if branch_result.is_err():
                branch_errors.extend(branch_result.unwrap_err())
            else:
                all_branches.append(branch_result.unwrap())
        if branch_errors:
            return Err(branch_errors)
        result_elements: list[Element] = [Disjunction(branches=all_branches)]
        return Ok(result_elements)

    errors: list[str] = []
    elements: list[Element] = []

    i = 0
    while i < len(text):
        ch = text[i]

        # Skip whitespace
        if ch in (" ", "\t"):
            i += 1
            continue

        # Word boundary
        if ch == "#":
            elements.append(Boundary(kind="word"))
            i += 1
            continue

        # Syllable boundary
        if ch == "$":
            elements.append(Boundary(kind="syllable"))
            i += 1
            continue

        # Null segment (∅ U+2205 or 0)
        if ch == "∅" or ch == "0":
            elements.append(Null())
            i += 1
            continue

        # Negation prefix before bracket
        if ch == "!":
            if i + 1 < len(text) and text[i + 1] == "[":
                # Negated bundle: ![...]
                end = text.find("]", i + 1)
                if end == -1:
                    errors.append(f"Unclosed bracket in {label} after '!' at position {i}")
                    break
                inner = text[i + 2 : end].strip()
                bundle_result = FeatureBundle.from_str(inner, inventory)
                if bundle_result.is_err():
                    errors.extend(bundle_result.unwrap_err())
                    i = end + 1
                else:
                    quant, next_i = _parse_quantifier(text, end + 1)
                    elements.append(Bundle(bundle=bundle_result.unwrap(), quantifier=quant, negated=True))
                    i = next_i
                continue
            else:
                errors.append(f"'!' in {label} must be followed by '[' at position {i}")
                break

        # Feature bundle in brackets
        if ch == "[":
            end = text.find("]", i)
            if end == -1:
                errors.append(f"Unclosed bracket in {label} starting at position {i}")
                break
            inner = text[i + 1 : end].strip()
            bundle_result = FeatureBundle.from_str(inner, inventory)
            if bundle_result.is_err():
                errors.extend(bundle_result.unwrap_err())
                i = end + 1
            else:
                quant, next_i = _parse_quantifier(text, end + 1)
                elements.append(Bundle(bundle=bundle_result.unwrap(), quantifier=quant))
                i = next_i
            continue

        # Group in parentheses
        if ch == "(":
            end = _find_matching_bracket(text, i, "(", ")")
            if end == -1:
                errors.append(f"Unclosed parenthesis in {label} starting at position {i}")
                break
            inner = text[i + 1 : end].strip()
            inner_result = _parse_element_list(inner, inventory, f"{label} group")
            if inner_result.is_err():
                errors.extend(inner_result.unwrap_err())
                i = end + 1
            else:
                quant, next_i = _parse_quantifier(text, end + 1)
                elements.append(Group(elements=inner_result.unwrap(), quantifier=quant))
                i = next_i
            continue

        # Reference: @identifier
        if ch == "@":
            # Read identifier: one or more alphanumeric characters
            j = i + 1
            while j < len(text) and (text[j].isalnum() or text[j] == "_"):
                j += 1
            if j == i + 1:
                errors.append(f"'@' in {label} must be followed by an identifier at position {i}")
                break
            name = text[i + 1 : j]
            elements.append(Ref(name=name))
            i = j
            continue

        # Binding: identifier= before [ or ( — captures the matched span
        # Identifier pattern: starts with uppercase letter or letter, continues with alphanumeric
        if ch.isalpha():
            # Read the potential identifier
            j = i
            while j < len(text) and (text[j].isalnum() or text[j] == "_"):
                j += 1
            # Check if followed by =
            if j < len(text) and text[j] == "=":
                name = text[i:j]
                # Parse what follows = as a pattern element
                k = j + 1  # skip the =
                if k >= len(text):
                    errors.append(f"Binding '{name}=' in {label} must be followed by an element at position {j}")
                    break
                next_ch = text[k]

                # Skip whitespace after =
                while k < len(text) and text[k] in (" ", "\t"):
                    k += 1
                if k >= len(text):
                    errors.append(f"Binding '{name}=' in {label} must be followed by an element at position {j}")
                    break
                next_ch = text[k]

                if next_ch == "[":
                    end = text.find("]", k)
                    if end == -1:
                        errors.append(f"Unclosed bracket in {label} after binding '{name}=' at position {k}")
                        break
                    inner = text[k + 1 : end].strip()
                    bundle_result = FeatureBundle.from_str(inner, inventory)
                    if bundle_result.is_err():
                        errors.extend(bundle_result.unwrap_err())
                        i = end + 1
                    else:
                        quant, next_i = _parse_quantifier(text, end + 1)
                        pattern: list[Element] = [Bundle(bundle=bundle_result.unwrap(), quantifier=quant)]
                        elements.append(Binding(name=name, pattern=pattern))
                        i = next_i
                elif next_ch == "(":
                    end = _find_matching_bracket(text, k, "(", ")")
                    if end == -1:
                        errors.append(f"Unclosed parenthesis in {label} after binding '{name}=' at position {k}")
                        break
                    inner = text[k + 1 : end].strip()
                    inner_result = _parse_element_list(inner, inventory, f"{label} binding group")
                    if inner_result.is_err():
                        errors.extend(inner_result.unwrap_err())
                        i = end + 1
                    else:
                        quant, next_i = _parse_quantifier(text, end + 1)
                        # Wrap group content in a Group element
                        group: Element = Group(elements=inner_result.unwrap(), quantifier=quant)
                        pattern: list[Element] = [group]
                        elements.append(Binding(name=name, pattern=pattern))
                        i = next_i
                else:
                    errors.append(f"Binding '{name}=' in {label} must be followed by '[' or '(' at position {k}")
                    break
                continue
            # Not a binding — fall through to "unrecognised"

        # Unrecognised character
        errors.append(
            f"Unexpected character '{ch}' in {label} at position {i}"
        )
        break

    if errors:
        return Err(errors)
    return Ok(elements)


def _parse_context(
    context_str: str, inventory: FeatureInventory
) -> Result[tuple[list[Element] | None, list[Element] | None], list[str]]:
    """Parse a context string (after '/') into left and right context.

    The context string must contain ``_`` marking the target position.
    Everything before ``_`` is the left context; everything after ``_`` is
    the right context.

    ``#`` at the start/end indicates a word boundary.

    Returns (left_context, right_context).  Either may be None if that side
    is empty (meaning "unconstrained").
    """
    errors: list[str] = []
    underscore_pos = context_str.find("_")
    if underscore_pos == -1:
        errors.append("Context must contain '_' to mark the target position")
        return Err(errors)

    left_str = context_str[:underscore_pos].strip()
    right_str = context_str[underscore_pos + 1 :].strip()

    left_ctx = _parse_context_side(left_str, inventory, "left", errors)
    right_ctx = _parse_context_side(right_str, inventory, "right", errors)

    if errors:
        return Err(errors)
    return Ok((left_ctx, right_ctx))


def _parse_context_side(
    side_str: str,
    inventory: FeatureInventory,
    side_label: str,
    errors: list[str],
) -> list[Element] | None:
    """Parse one side of a context string.

    Returns a list of Elements, or None if the side is empty (unconstrained).
    ``#`` at the start or end is converted to a Boundary element.

    Disjunction (``|``) splits the side into branches, each parsed separately.
    The result is wrapped in a ``Disjunction`` element.
    """
    if not side_str:
        return None

    # Check for disjunction (|) at depth 0
    branches_text = _split_on_pipe(side_str)
    if len(branches_text) > 1:
        all_branches: list[list[Element]] = []
        for branch_text in branches_text:
            branch_result = _parse_context_side(branch_text, inventory, side_label, errors)
            if branch_result is not None:
                all_branches.append(branch_result)
            else:
                all_branches.append([])
        if all_branches:
            return [Disjunction(branches=all_branches)]
        return None

    # Check for boundary markers
    # # at the start of left context or end of right context
    has_boundary = False
    work = side_str

    if side_label == "left" and work.startswith("#"):
        has_boundary = True
        work = work[1:].strip()
    elif side_label == "right" and work.endswith("#"):
        has_boundary = True
        work = work[:-1].strip()

    # Parse the remaining string as element list
    # For left context, reverse the element order so that index 0 is the
    # segment nearest to the target (adjacent-first ordering).
    elements: list[Element] = []
    if work:
        # Extract bracket groups and boundaries
        i = 0
        while i < len(work):
            ch = work[i]

            if ch in (" ", "\t"):
                i += 1
                continue

            # Syllable boundary
            if ch == "$":
                elements.append(Boundary(kind="syllable"))
                i += 1
                continue

            # Null segment (∅ U+2205 or 0)
            if ch == "∅" or ch == "0":
                elements.append(Null())
                i += 1
                continue

            # Negation prefix before bracket
            if ch == "!":
                if i + 1 < len(work) and work[i + 1] == "[":
                    end = work.find("]", i + 1)
                    if end == -1:
                        errors.append(f"Unclosed bracket in {side_label} context after '!' at position {i}")
                        return elements if elements else None
                    inner = work[i + 2 : end].strip()
                    bundle_result = FeatureBundle.from_str(inner, inventory)
                    if bundle_result.is_err():
                        errors.extend(bundle_result.unwrap_err())
                        i = end + 1
                    else:
                        quant, next_i = _parse_quantifier(work, end + 1)
                        elements.append(Bundle(bundle=bundle_result.unwrap(), quantifier=quant, negated=True))
                        i = next_i
                    continue
                else:
                    errors.append(f"'!' in {side_label} context must be followed by '[' at position {i}")
                    break

            if ch == "[":
                end = work.find("]", i)
                if end == -1:
                    errors.append(f"Unclosed bracket in {side_label} context at position {i}")
                    return elements if elements else None
                inner = work[i + 1 : end].strip()
                bundle_result = FeatureBundle.from_str(inner, inventory)
                if bundle_result.is_err():
                    errors.extend(bundle_result.unwrap_err())
                    i = end + 1
                else:
                    quant, next_i = _parse_quantifier(work, end + 1)
                    elements.append(Bundle(bundle=bundle_result.unwrap(), quantifier=quant))
                    i = next_i
                continue

            # Group in parentheses
            if ch == "(":
                end = _find_matching_bracket(work, i, "(", ")")
                if end == -1:
                    errors.append(f"Unclosed parenthesis in {side_label} context at position {i}")
                    return elements if elements else None
                inner = work[i + 1 : end].strip()
                inner_result = _parse_element_list(inner, inventory, f"{side_label} context group")
                if inner_result.is_err():
                    errors.extend(inner_result.unwrap_err())
                    i = end + 1
                else:
                    quant, next_i = _parse_quantifier(work, end + 1)
                    elements.append(Group(elements=inner_result.unwrap(), quantifier=quant))
                    i = next_i
                continue

            # Shouldn't have # here (already stripped)
            if ch == "#":
                errors.append(f"Misplaced '#' in {side_label} context (boundary markers must be at the outermost edge)")
                i += 1
                continue

            # Reference: @identifier
            if ch == "@":
                j = i + 1
                while j < len(work) and (work[j].isalnum() or work[j] == "_"):
                    j += 1
                if j == i + 1:
                    errors.append(f"'@' in {side_label} context must be followed by an identifier at position {i}")
                    break
                name = work[i + 1 : j]
                elements.append(Ref(name=name))
                i = j
                continue

            # Binding: identifier= before [ or (
            if ch.isalpha():
                j = i
                while j < len(work) and (work[j].isalnum() or work[j] == "_"):
                    j += 1
                if j < len(work) and work[j] == "=":
                    name = work[i:j]
                    k = j + 1
                    while k < len(work) and work[k] in (" ", "\t"):
                        k += 1
                    if k >= len(work):
                        errors.append(f"Binding '{name}=' in {side_label} context must be followed by an element")
                        break
                    next_ch = work[k]
                    if next_ch == "[":
                        end = work.find("]", k)
                        if end == -1:
                            errors.append(f"Unclosed bracket in {side_label} context after binding '{name}='")
                            break
                        inner = work[k + 1 : end].strip()
                        bundle_result = FeatureBundle.from_str(inner, inventory)
                        if bundle_result.is_err():
                            errors.extend(bundle_result.unwrap_err())
                            i = end + 1
                        else:
                            quant, next_i = _parse_quantifier(work, end + 1)
                            pattern: list[Element] = [Bundle(bundle=bundle_result.unwrap(), quantifier=quant)]
                            elements.append(Binding(name=name, pattern=pattern))
                            i = next_i
                    elif next_ch == "(":
                        end = _find_matching_bracket(work, k, "(", ")")
                        if end == -1:
                            errors.append(f"Unclosed parenthesis in {side_label} context after binding '{name}='")
                            break
                        inner = work[k + 1 : end].strip()
                        inner_result = _parse_element_list(inner, inventory, f"{side_label} context binding group")
                        if inner_result.is_err():
                            errors.extend(inner_result.unwrap_err())
                            i = end + 1
                        else:
                            quant, next_i = _parse_quantifier(work, end + 1)
                            group_elem: Element = Group(elements=inner_result.unwrap(), quantifier=quant)
                            pattern = [group_elem]
                            elements.append(Binding(name=name, pattern=pattern))
                            i = next_i
                    else:
                        errors.append(f"Binding '{name}=' in {side_label} context must be followed by '[' or '('")
                        break
                    continue
                # Not a binding — fall through to error

            errors.append(
                f"Unexpected character '{ch}' in {side_label} context"
            )
            break

    # Left context: reverse to adjacent-first order
    if side_label == "left":
        # The SPE notation writes left-to-right (away from target),
        # but we want nearest-first.
        elements.reverse()

    if has_boundary:
        # Boundary always goes at the outermost edge of the context.
        # For left context (already reversed to adjacent-first order),
        #   the outermost edge is the end of the list.
        # For right context (already in adjacent-first order),
        #   the outermost edge is also the end of the list.
        elements.append(Boundary(kind="word"))

    return elements
