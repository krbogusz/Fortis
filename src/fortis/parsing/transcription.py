from src.fortis.config import config
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.inventories import Inventories
from src.fortis.models.sequence import Sequence


def string_to_sequence(raw_string: str, inventories: Inventories) -> Sequence:
    """Turn IPA strings into lists of segments.

    Uses greedy longest-first matching so that multi-character symbols
    (e.g. "t͡s", "ːː") are consumed before their shorter prefixes.

    Args:
        raw_string: Raw IPA string.
        inventories: Inventories.
    """
    segments: list[FeatureBundle] = []
    buffer: FeatureBundle = FeatureBundle(inventory=inventories.features)
    i = 0

    while i < len(raw_string):
        remaining = raw_string[i:]

        # 1. Before diacritics (accumulated in buffer)
        for diacritic_symbol in inventories.before_diacritic_keys:
            if remaining.startswith(diacritic_symbol):
                diacritic = inventories.diacritics[diacritic_symbol]
                buffer = buffer.combine_with(diacritic.bundle, form_contours=diacritic.contour)
                i += len(diacritic_symbol)
                break
        else:
            # 2. Letters (combine with buffered before-diacritics)
            for letter_symbol in inventories.letter_keys:
                if remaining.startswith(letter_symbol):
                    segment = inventories.letters[letter_symbol]
                    segment = segment.combine_with(buffer)
                    segments.append(segment)
                    buffer = FeatureBundle(inventory=inventories.features)
                    i += len(letter_symbol)
                    break
            else:
                # 3. Attaching diacritics (combining + after)
                for diacritic_symbol in inventories.attaching_diacritic_keys:
                    if remaining.startswith(diacritic_symbol):
                        diacritic = inventories.diacritics[diacritic_symbol]
                        segments[-1] = segments[-1].combine_with(diacritic.bundle, form_contours=diacritic.contour)
                        i += len(diacritic_symbol)
                        break
                else:
                    for reserved_symbol in config.reserved_symbols:
                        if remaining.startswith(reserved_symbol):
                            i += len(reserved_symbol)
                            break
                    else:
                        raise ValueError(f"Unknown character '{raw_string[i]}' at position {i}")
    return Sequence(segments)
