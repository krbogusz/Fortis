from src.fortis.config import config
from src.fortis.imports.inventories import Inventories
from src.fortis.models.feature_bundle import FeatureBundle


def string_to_sequence(raw_string: str, inventories: Inventories) -> list[FeatureBundle]:
    """Turn IPA strings into lists of segments.

    Uses greedy longest-first matching so that multi-character symbols
    (e.g. "t͡s", "ːː") are consumed before their shorter prefixes.

    Args:
        raw_string: Raw IPA string.
        inventories: Inventories.
    """
    segments: list[FeatureBundle] = []
    buffer: FeatureBundle = FeatureBundle()
    syllable_buffer: FeatureBundle = FeatureBundle()
    last_nucleus_index = -1
    i = 0

    while i < len(raw_string):
        remaining = raw_string[i:]

        # 1. Before diacritics (accumulated in buffers)
        for diacritic_symbol in inventories.before_diacritic_keys:
            if remaining.startswith(diacritic_symbol):
                diacritic_def = inventories.diacritics[diacritic_symbol]
                if diacritic_symbol in inventories.syllable_diacritic_keys:
                    syllable_buffer = syllable_buffer.combine_with(
                        diacritic_def.bundle, form_contours=diacritic_def.contour
                    )
                else:
                    buffer = buffer.combine_with(diacritic_def.bundle, form_contours=diacritic_def.contour)
                i += len(diacritic_symbol)
                break
        else:
            # 2. Letters (combine with buffered before-diacritics)
            for letter_symbol in inventories.letter_keys:
                if remaining.startswith(letter_symbol):
                    segment = inventories.letters[letter_symbol].bundle
                    segment = segment.combine_with(buffer)
                    nucleus = inventories.syllable_parts.get_nucleus(inventories.time)
                    if nucleus is not None and segment.matches_pattern(nucleus):
                        segment = segment.combine_with(syllable_buffer)
                        last_nucleus_index = len(segments) - 1
                        syllable_buffer = FeatureBundle()
                    segments.append(segment)
                    buffer = FeatureBundle()
                    i += len(letter_symbol)
                    break
            else:
                # 3. Attaching diacritics (combining + after)
                for diacritic_symbol in inventories.attaching_diacritic_keys:
                    if remaining.startswith(diacritic_symbol):
                        diacritic_def = inventories.diacritics[diacritic_symbol]
                        if diacritic_symbol in inventories.syllable_diacritic_keys:
                            segments[last_nucleus_index] = segments[last_nucleus_index].combine_with(
                                diacritic_def.bundle, form_contours=diacritic_def.contour
                            )
                        else:
                            segments[-1] = segments[-1].combine_with(
                                diacritic_def.bundle, form_contours=diacritic_def.contour
                            )
                        i += len(diacritic_symbol)
                        break
                else:
                    for reserved_symbol in config.reserved_symbols:
                        if remaining.startswith(reserved_symbol):
                            i += len(reserved_symbol)
                            break
                    else:
                        raise ValueError(f"Unknown character '{raw_string[i]}' at position {i}")
    return segments
