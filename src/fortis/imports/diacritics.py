from collections import UserDict
from dataclasses import dataclass
from enum import StrEnum, auto
from pathlib import Path
from typing import Any

from src.fortis.general.file_handling import load_toml_file
from src.fortis.general.presentation import present_symbol
from src.fortis.imports.features import FeatureInventory
from src.fortis.parsing import parse_feature_bundle
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.tier import Tier
from src.fortis.result import Err, Ok, Result


class DiacriticType(StrEnum):
    """Where a diacritic attaches relative to its base symbol."""

    before = auto()
    combining = auto()
    after = auto()


@dataclass
class DiacriticDefinition:
    """A diacritic symbol with its tier, attachment type, and feature bundle.

    Args:
        symbol: The diacritic character(s).
        tier: Phonological tier this diacritic belongs to.
        type: Where the diacritic attaches relative to its base.
        bundle: Feature bundle the diacritic contributes.
        default: Whether this is the default diacritic for its features.
        contour: Whether this diacritic forms contours when combined.
    """

    symbol: str
    tier: Tier
    type: DiacriticType
    bundle: FeatureBundle
    default: bool
    contour: bool

    @classmethod
    def load(
        cls, symbol: str, diacritic_def: dict[str, Any], features: FeatureInventory
    ) -> Result[DiacriticDefinition, list[str]]:
        """Build a DiacriticDefinition from a raw TOML entry.

        Args:
            symbol: The diacritic character(s).
            diacritic_def: Raw dictionary from the TOML file.
            features: Feature inventory for bundle parsing.
        """
        error_list = []

        tier_result = cls._load_tier(symbol, diacritic_def)
        if tier_result.is_err():
            error_list.append(tier_result.unwrap_err())

        type_result = cls._load_type(symbol, diacritic_def)
        if type_result.is_err():
            error_list.append(type_result.unwrap_err())

        bundle_result = cls._load_bundle(symbol, diacritic_def, features)
        if bundle_result.is_err():
            error_list.extend(bundle_result.unwrap_err())

        default_result = cls._load_default(symbol, diacritic_def)
        if default_result.is_err():
            error_list.append(default_result.unwrap_err())

        contour_result = cls._load_contour(symbol, diacritic_def)
        if contour_result.is_err():
            error_list.append(contour_result.unwrap_err())

        if error_list:
            return Err(error_list)
        else:
            return Ok(
                DiacriticDefinition(
                    symbol=symbol,
                    tier=tier_result.unwrap(),
                    type=type_result.unwrap(),
                    bundle=bundle_result.unwrap(),
                    default=default_result.unwrap(),
                    contour=contour_result.unwrap(),
                )
            )

    # —— Loading helpers ——————————————————————————————————————————————————————————————————————————
    @staticmethod
    def _load_tier(symbol: str, diacritic_def: dict[str, Any]) -> Result[Tier, str]:
        """Parse and validate the 'tier' field.

        Args:
            symbol: Diacritic symbol (for error messages).
            diacritic_def: Raw dictionary from the TOML file.
        """
        value = diacritic_def.get("tier")
        if not value:
            return Err(f"Diacritic '{present_symbol(symbol)}' is missing required field 'tier'")
        try:
            tier = Tier(value.strip().lower())
        except ValueError:
            return Err(
                f"Diacritic '{present_symbol(symbol)}' has invalid tier '{value}'"
                + f"(expected {', '.join(t.value for t in Tier)})"
            )
        return Ok(tier)

    @staticmethod
    def _load_type(symbol: str, diacritic_def: dict[str, Any]) -> Result[DiacriticType, str]:
        """Parse and validate the 'type' field.

        Args:
            symbol: Diacritic symbol (for error messages).
            diacritic_def: Raw dictionary from the TOML file.
        """
        value = diacritic_def.get("type")
        if not value:
            return Err(f"Diacritic '{present_symbol(symbol)}' is missing required field 'type'")
        try:
            dtype = DiacriticType(value.strip().lower())
        except ValueError:
            return Err(
                f"Diacritic '{present_symbol(symbol)}' has invalid type '{value}' "
                + f"(expected {', '.join(t.value for t in DiacriticType)})"
            )
        return Ok(dtype)

    @staticmethod
    def _load_bundle(
        symbol: str, diacritic_def: dict[str, Any], features: FeatureInventory
    ) -> Result[FeatureBundle, list[str]]:
        """Parse the 'bundle' field; empty string yields None.

        Args:
            symbol: Diacritic symbol (for error messages).
            diacritic_def: Raw dictionary from the TOML file.
            features: Feature inventory for bundle parsing.
        """
        value = diacritic_def.get("bundle")
        if value is None:
            return Err([f"Diacritic '{present_symbol(symbol)}' is missing required field 'bundle'"])
        if value == "":
            return Err([f"Diacritic '{present_symbol(symbol)}' is missing required field 'bundle'"])
        bundle_result = parse_feature_bundle(value, features)
        if bundle_result.is_err():
            return Err(bundle_result.unwrap_err())
        return Ok(bundle_result.unwrap())

    @staticmethod
    def _load_default(symbol: str, diacritic_def: dict[str, Any]) -> Result[bool, str]:
        """Parse the optional 'default' field (defaults to False).

        Args:
            symbol: Diacritic symbol (for error messages).
            diacritic_def: Raw dictionary from the TOML file.
        """
        value = diacritic_def.get("default")
        if not value:
            return Ok(False)
        if not isinstance(value, bool):
            return Err(f"Diacritic '{present_symbol(symbol)}' 'default' must be 'true' or 'false'")
        return Ok(value)

    @staticmethod
    def _load_contour(symbol: str, diacritic_def: dict[str, Any]) -> Result[bool, str]:
        """Parse the optional 'contour' field (defaults to False).

        Args:
            symbol: Diacritic symbol (for error messages).
            diacritic_def: Raw dictionary from the TOML file.
        """
        value = diacritic_def.get("contour")
        if not value:
            return Ok(False)
        if not isinstance(value, bool):
            return Err(f"Diacritic '{present_symbol(symbol)}' 'contour' must be 'true' or 'false'")
        return Ok(value)


class DiacriticInventory(UserDict[str, DiacriticDefinition]):
    """Diacritic symbols mapped to their definitions.

    Pre-computes sorted symbol lists at construction time for greedy
    longest-first matching in IPA tokenisation.  Access them via the
    ``segment_keys``, ``syllable_keys``, ``before_keys``, and
    ``attaching_keys`` properties.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initiate the inventory."""
        super().__init__(*args, **kwargs)
        self._build_sorted_keys()

    def _build_sorted_keys(self) -> None:
        """Pre-compute sorted symbol lists for greedy longest-first matching."""
        segment_symbols = {s for s, d in self.data.items() if d.tier == Tier.segment}
        syllable_symbols = {s for s, d in self.data.items() if d.tier == Tier.syllable}
        before_symbols = {s for s, d in self.data.items() if d.type == DiacriticType.before}
        attaching_symbols = {s for s, d in self.data.items() if d.type != DiacriticType.before}

        self._segment_keys: list[str] = sorted(segment_symbols, key=len, reverse=True)
        self._syllable_keys: list[str] = sorted(syllable_symbols, key=len, reverse=True)
        self._before_keys: list[str] = sorted(before_symbols, key=len, reverse=True)
        self._attaching_keys: list[str] = sorted(attaching_symbols, key=len, reverse=True)

    @property
    def segment_keys(self) -> list[str]:
        """Segment-tier diacritic symbols sorted longest-first."""
        return self._segment_keys

    @property
    def syllable_keys(self) -> list[str]:
        """Syllable-tier diacritic symbols sorted longest-first."""
        return self._syllable_keys

    @property
    def before_keys(self) -> list[str]:
        """Before-type diacritic symbols sorted longest-first."""
        return self._before_keys

    @property
    def attaching_keys(self) -> list[str]:
        """Combining/after-type diacritic symbols sorted longest-first."""
        return self._attaching_keys

    @property
    def segment_dict(self) -> dict[str, DiacriticDefinition]:
        """Segment-tier diacritics as a dict (symbol → definition)."""
        return {s: d for s, d in self.data.items() if d.tier == Tier.segment}

    @property
    def syllable_dict(self) -> dict[str, DiacriticDefinition]:
        """Syllable-tier diacritics as a dict (symbol → definition)."""
        return {s: d for s, d in self.data.items() if d.tier == Tier.syllable}

    @classmethod
    def load(cls, path: Path, features: FeatureInventory) -> Result[DiacriticInventory, list[str]]:
        """Load all diacritics from a TOML file.

        Args:
            path: Path to the TOML file.
            features: Feature inventory for bundle parsing.
        """
        error_list = []

        data_result = load_toml_file(path)
        if data_result.is_err():
            return Err([data_result.unwrap_err()])
        data = data_result.unwrap()

        diacritic_inventory = {}
        for symbol, diacritic_def_dict in data.items():
            symbol = symbol.strip()
            if symbol in diacritic_inventory:
                error_list.append(f"Diacritic '{present_symbol(symbol)}' is already defined")
                continue

            diacritic_def_result = DiacriticDefinition.load(symbol, diacritic_def_dict, features)
            if diacritic_def_result.is_err():
                error_list.extend(diacritic_def_result.unwrap_err())
                continue

            diacritic_inventory[symbol] = diacritic_def_result.unwrap()

        if error_list:
            return Err(error_list)

        inv = cls(diacritic_inventory)
        check_result = inv.validate(features)
        if check_result.is_err():
            return Err(check_result.unwrap_err())

        return Ok(inv)

    def validate(self, features: FeatureInventory) -> Result[None, list[str]]:
        """Check for cross-diacritic consistency issues.

        Validates that each diacritic's bundle features match its declared tier.
        Duplicate bundles on the same tier and type are allowed — the same
        feature bundle may be expressed by multiple input symbols.
        """
        error_list: list[str] = []

        # Bundle-tier consistency
        for symbol, diacritic_def in self.data.items():
            for feature_name in diacritic_def.bundle:
                if feature_name not in features:
                    continue  # already caught during bundle parsing
                feature_tier = features[feature_name].tier
                if feature_tier != diacritic_def.tier:
                    error_list.append(
                        f"Diacritic '{present_symbol(symbol)}' (tier: {diacritic_def.tier.value}) "
                        f"uses feature '{feature_name}' which belongs to tier: {feature_tier.value}"
                    )

        if error_list:
            return Err(error_list)
        return Ok(None)
