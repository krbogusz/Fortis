from __future__ import annotations

from src.fortis.application.combining import combine
from src.fortis.application.matching import pattern_matches
from src.fortis.config import config
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.project import Project


def _is_nucleus(segment: FeatureBundle, project: Project) -> bool:
    """Whether *segment* matches the nucleus definition in force at the project time."""
    nucleus = project.syllable_parts.get_nucleus(project.time)
    return (
        nucleus is not None
        and nucleus.definition is not None
        and pattern_matches(nucleus.definition, segment)
    )


def string_to_sequence(raw_string: str, project: Project) -> list[FeatureBundle]:
    """Turn IPA strings into lists of segments.

    Uses greedy longest-first matching so that multi-character symbols
    (e.g. "t͡s", "ːː") are consumed before their shorter prefixes.

    Args:
        raw_string: Raw IPA string.
        project: Inventories and other dependencies.
    """
    segments: list[FeatureBundle] = []
    buffer: FeatureBundle = FeatureBundle()
    syllable_buffer: FeatureBundle = FeatureBundle()
    last_nucleus_index = -1
    i = 0

    while i < len(raw_string):
        remaining = raw_string[i:]

        # 1. Before diacritics (accumulated in buffers)
        for diacritic_symbol in project.diacritics.before_keys:
            if remaining.startswith(diacritic_symbol):
                diacritic_def = project.diacritics[diacritic_symbol]
                if diacritic_symbol in project.diacritics.syllable_keys:
                    syllable_buffer = combine(
                        syllable_buffer, diacritic_def.bundle, form_contours=diacritic_def.contour
                    )
                else:
                    buffer = combine(
                        buffer, diacritic_def.bundle, form_contours=diacritic_def.contour
                    )
                i += len(diacritic_symbol)
                break
        else:
            # 2. Letters (combine with buffered before-diacritics)
            for letter_symbol in project.letters.sorted_keys:
                if remaining.startswith(letter_symbol):
                    segment = project.letters[letter_symbol].bundle
                    segment = combine(segment, buffer)
                    if _is_nucleus(segment, project):
                        segment = combine(segment, syllable_buffer)
                        last_nucleus_index = len(segments)  # index the nucleus gets on append
                        syllable_buffer = FeatureBundle()
                    segments.append(segment)
                    buffer = FeatureBundle()
                    i += len(letter_symbol)
                    break
            else:
                # 3. Attaching diacritics (combining + after)
                for diacritic_symbol in project.diacritics.attaching_keys:
                    if remaining.startswith(diacritic_symbol):
                        diacritic_def = project.diacritics[diacritic_symbol]
                        if diacritic_symbol in project.diacritics.syllable_keys:
                            if last_nucleus_index < 0:
                                raise ValueError(
                                    f"Suprasegmental diacritic '{diacritic_symbol}' at "
                                    f"position {i} has no preceding nucleus to attach to"
                                )
                            segments[last_nucleus_index] = combine(
                                segments[last_nucleus_index],
                                diacritic_def.bundle,
                                form_contours=diacritic_def.contour,
                            )
                        else:
                            if not segments:
                                raise ValueError(
                                    f"Diacritic '{diacritic_symbol}' at position {i} "
                                    "has no preceding segment to attach to"
                                )
                            segments[-1] = combine(
                                segments[-1],
                                diacritic_def.bundle,
                                form_contours=diacritic_def.contour,
                            )
                            # A segment-tier diacritic (e.g. syllabic ̩) can turn the
                            # segment into a nucleus; if so, it claims any pending
                            # syllable-tier before-diacritics (e.g. stress) and becomes
                            # the current nucleus for later attaching diacritics.
                            if _is_nucleus(segments[-1], project):
                                if syllable_buffer:
                                    segments[-1] = combine(segments[-1], syllable_buffer)
                                    syllable_buffer = FeatureBundle()
                                last_nucleus_index = len(segments) - 1
                        i += len(diacritic_symbol)
                        break
                else:
                    for reserved_symbol in config.special_symbols:
                        if remaining.startswith(reserved_symbol):
                            i += len(reserved_symbol)
                            break
                    else:
                        raise ValueError(f"Unknown character '{raw_string[i]}' at position {i}")
    return segments
