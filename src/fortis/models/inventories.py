from dataclasses import dataclass, field
from pathlib import Path

from src.fortis.config import config
from src.fortis.models.diacritics import DiacriticDefinition, DiacriticInventory
from src.fortis.models.feature_definition import FeatureDefinition
from src.fortis.models.feature_inventory import FeatureInventory
from src.fortis.models.letters import LetterInventory
from src.fortis.models.sonorities import SonorityInventory
from src.fortis.models.syllable_settings import SyllableSettings
from src.fortis.models.tiers import Tier
from src.fortis.result import present_errors


@dataclass
class Inventories:
    """Top-level container holding all loaded inventories.

    Args:
        features: Feature definitions keyed by name.
        letters: Segment symbols keyed by their feature bundles.
        diacritics: Diacritic symbols keyed by their definitions.
        sonorities: Sonority levels keyed by label.
    """

    features: FeatureInventory
    letters: LetterInventory
    diacritics: DiacriticInventory
    sonorities: SonorityInventory
    syllable_settings: SyllableSettings

    # Pre-computed sorted symbol lists for greedy longest-first matching
    segment_diacritic_keys: list[str] = field(init=False, repr=False)
    syllable_diacritic_keys: list[str] = field(init=False, repr=False)
    before_diacritic_keys: list[str] = field(init=False, repr=False)
    letter_keys: list[str] = field(init=False, repr=False)
    attaching_diacritic_keys: list[str] = field(init=False, repr=False)

    def __post_init__(self):
        """Post inititation run."""
        segment_diacritics = self.segment_diacritics()
        syllable_diacritics = self.syllable_diacritics()

        before = {s for s, d in self.diacritics.items() if d.type == "before"}
        attaching = {s for s, d in self.diacritics.items() if d.type != "before"}

        self.segment_diacritic_keys = sorted(segment_diacritics, key=len, reverse=True)
        self.syllable_diacritic_keys = sorted(syllable_diacritics, key=len, reverse=True)
        self.before_diacritic_keys = sorted(before, key=len, reverse=True)
        self.letter_keys = sorted(self.letters, key=len, reverse=True)
        self.attaching_diacritic_keys = sorted(attaching, key=len, reverse=True)

    @classmethod
    def load(cls, inventories_dir: Path | None = None) -> Inventories:
        """Load all inventories from the given directory, or the configured default.

        Args:
            inventories_dir: Directory containing features.toml, letters.csv, etc.
                Falls back to ``config.paths.inventories`` if None.
        """
        dir_path = inventories_dir or config.paths.inventories
        features_result = FeatureInventory.load(dir_path / "features.toml")
        if features_result.is_err():
            raise ValueError(present_errors(features_result.unwrap_err()))

        features = features_result.unwrap()
        error_list = []

        letters_result = LetterInventory.load(dir_path / "letters.csv", features)
        if letters_result.is_err():
            error_list.extend(letters_result.unwrap_err())

        diacritics_result = DiacriticInventory.load(dir_path / "diacritics.toml", features)
        if diacritics_result.is_err():
            error_list.extend(diacritics_result.unwrap_err())

        sonorities_result = SonorityInventory.load(dir_path / "sonorities.toml", features)
        if sonorities_result.is_err():
            error_list.extend(sonorities_result.unwrap_err())

        syllable_settings_result = SyllableSettings.load(dir_path / "syllable_settings.toml", features)
        if syllable_settings_result.is_err():
            error_list.extend(syllable_settings_result.unwrap_err())

        if error_list:
            raise ValueError(present_errors(error_list))

        return cls(
            features=features,
            letters=letters_result.unwrap(),
            diacritics=diacritics_result.unwrap(),
            sonorities=sonorities_result.unwrap(),
            syllable_settings=syllable_settings_result.unwrap(),
        )

    def segment_features(self) -> dict[str, FeatureDefinition]:
        """Return a subset of just segmental features."""
        segment_features = {}
        for feature_name, feature_def in self.features.items():
            if feature_def.tier == Tier.segment:
                segment_features[feature_name] = feature_def
        return segment_features

    def syllable_features(self) -> dict[str, FeatureDefinition]:
        """Return a subset of just syllable features."""
        syllable_features = {}
        for feature_name, feature_def in self.features.items():
            if feature_def.tier == Tier.syllable:
                syllable_features[feature_name] = feature_def
        return syllable_features

    def segment_diacritics(self) -> dict[str, DiacriticDefinition]:
        """Return a subset of just segment diacritics."""
        segment_diacritics = {}
        for diacritic_symbol, diacritic_def in self.diacritics.items():
            if diacritic_def.tier == Tier.segment:
                segment_diacritics[diacritic_symbol] = diacritic_def
        return segment_diacritics

    def syllable_diacritics(self) -> dict[str, DiacriticDefinition]:
        """Return a subset of just syllable diacritics."""
        syllable_diacritics = {}
        for diacritic_symbol, diacritic_def in self.diacritics.items():
            if diacritic_def.tier == Tier.syllable:
                syllable_diacritics[diacritic_symbol] = diacritic_def
        return syllable_diacritics
