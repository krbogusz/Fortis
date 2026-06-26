"""Shared fixtures for Fortis tests."""

import pytest

from src.fortis.loaders.features import load_feature_inventory
from src.fortis.loaders.project import load_project
from src.fortis.models.features import FeatureInventory
from src.fortis.models.inventories import (
    SonoritiesInventory,
    Sonority,
    SyllablePart,
    SyllablePartsInventory,
)
from src.fortis.models.project import Project
from src.fortis.models.tier_declaration import TierDeclaration, TierInventory
from src.fortis.parsing.bundles import parse_pattern_bundle


@pytest.fixture(scope="session")
def project() -> Project:
    """The real project loaded from the repo's ``inventories/`` directory."""
    result = load_project()
    assert result.is_ok(), f"Failed to load project: {result.unwrap_err()}"
    return result.unwrap()

MINIMAL_FEATURES_TOML = """\
[consonantal]
tier = "segment"
kind = "binary"
short = "cons"

[sonorant]
tier = "segment"
kind = "binary"
short = "son"

[syllabic]
tier = "segment"
kind = "binary"
short = "syll"

[nasal]
tier = "segment"
kind = "binary"
short = "nas"

[lateral]
tier = "segment"
kind = "binary"
short = "lat"

[continuant]
tier = "segment"
kind = "binary"
short = "cont"

[labial]
tier = "segment"
kind = "binary"
short = "lab"

[rounded]
tier = "segment"
kind = "binary"
short = "rd"

[front]
tier = "segment"
kind = "binary"
short = "frnt"

[high]
tier = "segment"
kind = "binary"
short = "hi"

[voice]
tier = "segment"
kind = "binary"
short = "vc"

[glop]
tier = "segment"
kind = "binary"
short = "gl"

[tense]
tier = "segment"
kind = "binary"
short = "tns"

[stress]
tier = "syllable"
kind = "scalar"
short = "str"
values = { 1 = "primary", 2 = "secondary" }

[tone]
tier = "syllable"
kind = "scalar"
short = "t"
values = { 1 = "low", 2 = "mid", 3 = "high", 4 = "extra_high", 5 = "super_high" }

[length]
tier = "segment"
kind = "scalar"
short = "ln"
values = { 1 = "short", 2 = "long", 3 = "overlong" }

[manner]
tier = "segment"
kind = "unary"
short = "man"
children = ["continuant", "sonorant", "nasal", "lateral"]
"""


@pytest.fixture
def features(tmp_path) -> FeatureInventory:
    """A FeatureInventory loaded from minimal TOML data."""
    path = tmp_path / "features.toml"
    path.write_text(MINIMAL_FEATURES_TOML)
    result = load_feature_inventory(path)
    assert result.is_ok(), f"Failed to load features: {result.unwrap_err()}"
    return result.unwrap()


# Sonority scale in file order = first-match order (specific predicates before general).
_SONORITY_SCALE = [
    ("vowel", 7, "syllabic: +, consonantal: -"),
    ("rhotic", 5, "consonantal: +, sonorant: +, nasal: none, lateral: none"),
    ("lateral", 4, "consonantal: +, sonorant: +, lateral: +"),
    ("nasal", 3, "sonorant: +, nasal: +"),
    ("fricative", 2, "sonorant: -, continuant: +"),
    ("stop", 1, "sonorant: -"),
]


@pytest.fixture
def sonorities(features) -> SonoritiesInventory:
    """A sonority scale assigning levels by first-match in file order."""
    inv = SonoritiesInventory()
    for label, level, predicate in _SONORITY_SCALE:
        inv[label] = Sonority(
            label=label, level=level, bundle=parse_pattern_bundle(predicate, features).unwrap()
        )
    return inv


@pytest.fixture
def syllable_parts(features) -> SyllablePartsInventory:
    """Nucleus = any [+syll] segment, defined from time 0."""
    nucleus = SyllablePart("nucleus", 0, parse_pattern_bundle("+syll", features).unwrap())
    return SyllablePartsInventory({0: {"nucleus": nucleus}})


@pytest.fixture
def tiers(features) -> TierInventory:
    """Tone and stress live on their own tiers, anchored to the syllabic nucleus.

    Mirrors the repo's ``tiers.toml``: tone is a lexical melody (OCP on), stress is
    rule-placed (OCP off). Used by deriving tests that need the suprasegmentals lifted
    off the segment bundles so the tier writes and redock behave as in the real engine.
    """
    inv = TierInventory()
    anchor = parse_pattern_bundle("+syll", features).unwrap()
    inv["tone"] = TierDeclaration(
        name="tone", carries=("tone",), anchor=anchor, melody=True, ocp=True
    )
    inv["stress"] = TierDeclaration(
        name="stress", carries=("stress",), anchor=anchor, melody=False, ocp=False
    )
    return inv
