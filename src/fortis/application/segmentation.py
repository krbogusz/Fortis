from __future__ import annotations

from src.fortis.application.combining import combine
from src.fortis.application.matching import pattern_matches
from src.fortis.application.tiers import associate_tiers
from src.fortis.config import config
from src.fortis.models.autosegment import Autoseg, AutosegmentalTier
from src.fortis.models.bundles import FeatureBundle, morpheme_boundary_bundle
from src.fortis.models.form import Form
from src.fortis.models.project import Project
from src.fortis.models.tier_declaration import TierInventory
from src.fortis.models.tiers import Tier

# A floating tone in the lexicon is written ⟨◌◌́⟩ — a tone diacritic on a dotted-circle
# placeholder, in float brackets. The dotted circle (U+25CC) is the carrier and is ignored.
_FLOAT_OPEN, _FLOAT_CLOSE, _DOTTED_CIRCLE = "⟨", "⟩", "◌"


def _parse_float_tone(inner: str, project: Project) -> FeatureBundle:
    """The tone bundle of a floating-tone marker's inner text (its tone diacritics)."""
    bundle = FeatureBundle()
    for ch in inner:
        if ch == _DOTTED_CIRCLE or ch.isspace():
            continue
        if ch not in project.diacritics:
            marker = f"{_FLOAT_OPEN}{inner}{_FLOAT_CLOSE}"
            raise ValueError(f"floating tone '{marker}' has no diacritic '{ch}'")
        diacritic = project.diacritics[ch]
        bundle = combine(bundle, diacritic.bundle, form_contours=diacritic.contour)
    return bundle


def _add_floating_autoseg(
    form: Form, tone: FeatureBundle, position: tuple[int, str], tiers: TierInventory
) -> None:
    """Add a positioned floating autosegment carrying *tone* to the tier that declares it."""
    name = next((n for n, decl in tiers.items() if any(f in decl.carries for f in tone)), None)
    if name is None:
        return
    autoseg = Autoseg(tone, form.fresh_id())
    tier = form.tiers.setdefault(name, AutosegmentalTier())
    tier.autosegs.append(autoseg)
    tier.float_hosts[autoseg.id] = position


def _split_suprasegmentals(
    segment: FeatureBundle, project: Project
) -> tuple[FeatureBundle, FeatureBundle]:
    """Split *segment* into (segmental features, syllable-tier features).

    Used to take the suprasegmentals back off a segment that a diacritic has just stopped being
    a nucleus, so they can be re-offered to the syllable's real nucleus.
    """
    syllable = {
        name
        for name, feature in project.features.items()
        if feature.tier == Tier.syllable and name in segment.data
    }
    if not syllable:
        return segment, FeatureBundle()
    return (
        FeatureBundle({f: s for f, s in segment.items() if f not in syllable}),
        FeatureBundle({f: s for f, s in segment.items() if f in syllable}),
    )


def _is_nucleus(segment: FeatureBundle, project: Project) -> bool:
    """Whether *segment* matches the nucleus definition in force at the project time."""
    nucleus = project.syllable_parts.get_nucleus(project.time)
    return (
        nucleus is not None
        and nucleus.definition is not None
        and pattern_matches(nucleus.definition, segment)
    )


def string_to_sequence(raw_string: str, project: Project) -> Form:
    """Turn IPA strings into a ``Form`` (the segmental tier, each segment id-tagged).

    Uses greedy longest-first matching so that multi-character symbols
    (e.g. "t͡s", "ːː") are consumed before their shorter prefixes. This is the
    construction point where each segment is assigned its stable identity.

    Args:
        raw_string: Raw IPA string.
        project: Inventories and other dependencies.
    """
    segments: list[FeatureBundle] = []
    float_markers: list[tuple[FeatureBundle, tuple[int, str]]] = []
    buffer: FeatureBundle = FeatureBundle()
    syllable_buffer: FeatureBundle = FeatureBundle()
    last_nucleus_index = -1
    i = 0

    while i < len(raw_string):
        remaining = raw_string[i:]

        # 0. A floating tone ⟨◌◌́⟩ — a tier autosegment with no anchor, positioned by where it
        #    sits: after the last segment so far, or before the first (a word-initial float).
        if remaining.startswith(_FLOAT_OPEN):
            close = remaining.find(_FLOAT_CLOSE)
            if close == -1:
                raise ValueError(f"unterminated floating tone '{_FLOAT_OPEN}' at position {i}")
            tone = _parse_float_tone(remaining[1:close], project)
            position = (len(segments) - 1, "after") if segments else (0, "before")
            float_markers.append((tone, position))
            i += close + 1
            continue

        # 0b. A morpheme boundary ``-`` — a real, deletable segment that forces a syllable
        #     break. It is its own segment, carries no phonological features, and is only
        #     ever matched by a ``-`` rule element.
        if remaining.startswith("-"):
            segments.append(morpheme_boundary_bundle())
            i += 1
            continue

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
                            else:
                                # …and it can do the reverse. A non-syllabic ̯ turns a diphthong's
                                # on-glide back into a non-nucleus — but the LETTER was a nucleus
                                # when it was appended, so it has already claimed the pending
                                # stress above. Left there, the stress sits on a non-syllabic
                                # segment, no tier can anchor it (`anchor: +syllabic`), and
                                # `stray_erase` deletes it: `ˈɲaws` keeps its stress while
                                # `ˈɲe̯aws` silently loses it — in the lexicon's ATTESTED forms as
                                # much as in derived ones, since targets are ingested through here.
                                # Hand the suprasegmentals BACK so the syllable's real nucleus
                                # claims them. The exact mirror of the clause above: a diacritic
                                # may make a nucleus, and it may just as well unmake one.
                                segments[-1], returned = _split_suprasegmentals(
                                    segments[-1], project
                                )
                                if returned:
                                    syllable_buffer = combine(syllable_buffer, returned)
                                if last_nucleus_index == len(segments) - 1:
                                    last_nucleus_index = next(
                                        (
                                            j
                                            for j in range(len(segments) - 2, -1, -1)
                                            if _is_nucleus(segments[j], project)
                                        ),
                                        -1,
                                    )
                        i += len(diacritic_symbol)
                        break
                else:
                    for reserved_symbol in config.special_symbols:
                        if remaining.startswith(reserved_symbol):
                            i += len(reserved_symbol)
                            break
                    else:
                        raise ValueError(f"Unknown character '{raw_string[i]}' at position {i}")
    form = Form.from_bundles(segments)
    form = associate_tiers(form, project.tiers)
    for tone, position in float_markers:
        _add_floating_autoseg(form, tone, position, project.tiers)
    return form
