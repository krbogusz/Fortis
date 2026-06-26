"""Smoke test for the tonal showcase (examples/tonal) — spread + stability on real data."""

from pathlib import Path

from src.fortis.application.deriving import derive, resolve_rule_letters
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.loaders.project import load_project

_EXAMPLE = Path(__file__).resolve().parent.parent / "examples" / "tonal"


def test_tonal_example_runs_and_preserves_tone():
    project = load_project(_EXAMPLE).unwrap()
    assert set(project.words) == {"táka", "katá"}  # high = combining acute
    rules = resolve_rule_letters(project.rules, project)
    for ipa, word in project.words.items():
        form = string_to_sequence(ipa, project)
        result = derive(
            word,
            form,
            rules,
            project.letters,
            project.features,
            project.sonorities,
            project.syllable_parts,
            project.tiers,
        )
        assert result.steps  # a rule fired
        surface_tones = [b["tone"].value for b in lower_tiers(result.surface) if "tone" in b]
        assert surface_tones == [4]  # exactly one high tone survives to the surface
