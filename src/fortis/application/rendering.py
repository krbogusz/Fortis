from src.fortis.loaders.inventories import Inventories
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.inventories import Diacritic, DiacriticKind


def sequence_to_string(sequence: list[FeatureBundle], inventories: Inventories) -> str:
    """Turn a Sequence of FeatureBundles back into an IPA string.

    For each segment:
    1. If it matches a letter exactly, output the letter.
    2. Otherwise, find the letter whose differences can be best covered
       by diacritics (fewest remaining differences after diacritic search).
    3. Output: before-diacritics + letter + combining-diacritics + after-diacritics.

    Suprasegmental (syllable-tier) diacritics are not yet handled.
    """
    output = ""
    for segment in sequence:
        output += render_segment(segment, inventories)
    return output


def render_segment(segment: FeatureBundle, inventories: Inventories) -> str:
    """Render a single FeatureBundle as an IPA string (letter + diacritics)."""
    # 1. Try exact match first
    for letter_symbol, letter_def in inventories.letters.items():
        if segment.matches_exactly(letter_def.bundle):
            return letter_symbol

    # 2. Find the best letter: the one whose differences leave the
    #    fewest remaining features after applying diacritics.
    #    Break ties by fewest total differences.
    best_symbol = None
    best_remaining = float("inf")
    best_total_diffs = float("inf")
    best_diacritics: tuple[list[str], list[str], list[str]] | None = None

    segment_diacritics = inventories.diacritics.segment_dict

    for letter_symbol, letter_def in inventories.letters.items():
        total_diffs = segment.differing(letter_def.bundle)
        remaining = set(total_diffs)
        before: list[str] = []
        combining: list[str] = []
        after: list[str] = []
        _find_diacritics(segment, remaining, segment_diacritics, before, combining, after)

        if (len(remaining) < best_remaining) or (
            len(remaining) == best_remaining and len(total_diffs) < best_total_diffs
        ):
            best_symbol = letter_symbol
            best_remaining = len(remaining)
            best_total_diffs = len(total_diffs)
            best_diacritics = (before, combining, after)

    if best_symbol is None:
        return "�"

    if best_diacritics is None:
        return "�"

    before, combining, after = best_diacritics
    return "".join(before) + best_symbol + "".join(combining) + "".join(after)


def _find_diacritics(
    target_bundle: FeatureBundle,
    remaining_diffs: set[str],
    diacritics: dict[str, DiacriticDefinition],
    before: list[str],
    combining: list[str],
    after: list[str],
) -> None:
    """Greedily find diacritics that cover the remaining feature differences.

    Each iteration picks the diacritic that covers the most remaining
    differences. A diacritic fits when all of its features exist in the
    target bundle with matching values. The search repeats until no
    diacritic can fill any remaining gap.
    """
    while remaining_diffs:
        best_symbol: str | None = None
        best_def: DiacriticDefinition | None = None
        best_coverage = 0

        for dia_symbol, dia_def in diacritics.items():
            dia_features = set(dia_def.bundle.keys())
            if not dia_features:
                continue

            # Every feature in the diacritic must exist in the target
            # with the same value (otherwise the diacritic would create
            # a new difference or express the wrong value).
            fits = True
            for feature, value in dia_def.bundle.items():
                if feature not in target_bundle or value.value != target_bundle[feature].value:
                    fits = False
                    break
            if not fits:
                continue

            # At least one feature must still be needed
            coverage = len(dia_features & remaining_diffs)
            if coverage == 0:
                continue

            # Prefer diacritics that cover more remaining differences;
            # break ties by preferring default diacritics
            if coverage > best_coverage or (
                coverage == best_coverage and best_def is not None and dia_def.default and not best_def.default
            ):
                best_symbol = dia_symbol
                best_def = dia_def
                best_coverage = coverage

        if best_def is None or best_symbol is None:
            # No diacritic can fill any remaining gap — stop
            break

        remaining_diffs -= set(best_def.bundle.keys())
        if best_def.type == DiacriticKind.before:
            before.append(best_symbol)
        elif best_def.type == DiacriticKind.combining:
            combining.append(best_symbol)
        else:
            after.append(best_symbol)
