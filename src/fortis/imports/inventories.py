from dataclasses import dataclass
from pathlib import Path

from src.fortis.config import config
from src.fortis.imports.diacritics import DiacriticInventory
from src.fortis.imports.features import FeatureDefinition, FeatureInventory
from src.fortis.imports.letters import LetterInventory
from src.fortis.imports.rules import RuleInventory
from src.fortis.imports.sonorities import SonorityInventory
from src.fortis.imports.syllable_parts import SyllablePartsInventory
from src.fortis.imports.words import WordInventory
from src.fortis.models.tier import Tier


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
    syllable_parts: SyllablePartsInventory
    words: WordInventory
    rules: RuleInventory
    time: int = 0

    @property
    def earliest_time(self) -> int:
        """The earliest time across all time-keyed inventories (syllable parts, rules)."""
        times: set[int] = set()
        if self.syllable_parts:
            times.update(self.syllable_parts.keys())
        if self.rules:
            times.update(rule.time for rule in self.rules.values())
        return min(times) if times else 0

    def __post_init__(self):
        """Post-initiation run."""
        self.time = self.earliest_time

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
            raise ValueError(features_result.unwrap_err())

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

        syllable_settings_result = SyllablePartsInventory.load(dir_path / "syllable_parts.toml", features)
        if syllable_settings_result.is_err():
            error_list.extend(syllable_settings_result.unwrap_err())

        words_result = WordInventory.load(dir_path / "words.toml")
        if words_result.is_err():
            error_list.extend(words_result.unwrap_err())

        rules_result = RuleInventory.load(dir_path / "rules.toml")
        if rules_result.is_err():
            error_list.extend(rules_result.unwrap_err())

        if error_list:
            raise ValueError(error_list)

        return cls(
            features=features,
            letters=letters_result.unwrap(),
            diacritics=diacritics_result.unwrap(),
            sonorities=sonorities_result.unwrap(),
            syllable_parts=syllable_settings_result.unwrap(),
            words=words_result.unwrap(),
            rules=rules_result.unwrap(),
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
