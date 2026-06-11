"""Shared fixtures for Fortis tests."""

import pytest

from src.fortis.loaders.features import load_feature_inventory
from src.fortis.models.features import Feature, FeatureInventory, FeatureKind
from src.fortis.models.tiers import Tier


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