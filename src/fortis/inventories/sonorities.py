from collections import UserDict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from src.fortis.general.file_handling import load_toml_file
from src.fortis.inventories.feature_inventory import FeatureInventory
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.result import Err, Ok, Result


@dataclass
class SonorityDefinition:
    """A sonority level with its feature bundle and nucleus flag.

    Args:
        label: Name/label of this sonority level.
        level: Numerical sonority level (higher = more sonorous).
        bundle: Feature bundle for this level, or None.
        nucleus: Whether this level counts as a syllable nucleus.
    """

    label: str
    level: int
    bundle: FeatureBundle | None

    @classmethod
    def load(
        cls, label: str, sonority_def_dict: dict[str, Any], inventory: FeatureInventory
    ) -> Result[SonorityDefinition, list[str]]:
        """Build a SonorityDefinition from a raw TOML entry.

        Args:
            label: Name/label of this sonority level.
            sonority_def_dict: Raw dictionary from the TOML file.
            inventory: Feature inventory for bundle parsing.
        """
        error_list = []

        level_result = cls._load_level(label, sonority_def_dict)
        if level_result.is_err():
            error_list.append(level_result.unwrap_err())

        bundle_result = cls._load_bundle(label, sonority_def_dict, inventory)
        if bundle_result.is_err():
            error_list.extend(bundle_result.unwrap_err())

        if error_list:
            return Err(error_list)
        else:
            return Ok(
                SonorityDefinition(
                    label,
                    level_result.unwrap(),
                    bundle_result.unwrap(),
                )
            )

    # —— Loading helpers ——————————————————————————————————————————————————————————————————————————
    @staticmethod
    def _load_level(label: str, sonority_def_dict: dict[str, Any]) -> Result[int, str]:
        """Parse and validate the 'level' field.

        Args:
            label: Sonority label (for error messages).
            sonority_def_dict: Raw dictionary from the TOML file.
        """
        value = sonority_def_dict.get("level")
        if not value:
            return Err(f"Sonority '{label}' is missing required field 'level'")
        try:
            level = int(value)
        except ValueError:
            return Err(f"Sonority '{label}' has invalid level '{value}'")
        return Ok(level)

    @staticmethod
    def _load_bundle(
        label: str, sonority_def_dict: dict[str, Any], inventory: FeatureInventory
    ) -> Result[FeatureBundle | None, list[str]]:
        """Parse the 'feature_bundle' field; empty string yields None.

        Args:
            label: Sonority label (for error messages).
            sonority_def_dict: Raw dictionary from the TOML file.
            inventory: Feature inventory for bundle parsing.
        """
        value = sonority_def_dict.get("feature_bundle")
        if value is None:
            return Err([f"Sonority '{label}' is missing required field 'feature_bundle'"])
        if value == "":
            return Ok(None)
        bundle_result = FeatureBundle.from_str(value, inventory, bare_unary_means_present=True)
        if bundle_result.is_err():
            return Err(bundle_result.unwrap_err())
        return Ok(bundle_result.unwrap())


class SonorityInventory(UserDict[str, SonorityDefinition]):
    """Sonority levels keyed by label."""

    def _sort_by_specificity(self):
        """Sort definitions by specificity for matching (most specific first).

        More features in the bundle means more specific; higher level breaks ties.
        """
        self._sorted: list[SonorityDefinition] = sorted(
            self.data.values(),
            key=lambda d: (-(len(d.bundle) if d.bundle else 0), -d.level),
        )

    @classmethod
    def load(cls, path: Path, inventory: FeatureInventory) -> Result[SonorityInventory, list[str]]:
        """Load sonority levels from a TOML file.

        Args:
            path: Path to the TOML file.
            inventory: Feature inventory for bundle parsing.
        """
        error_list = []

        data_result = load_toml_file(path)
        if data_result.is_err():
            return Err([data_result.unwrap_err()])
        data = data_result.unwrap()

        sonority_inventory = {}
        for label, sonority_def_dict in data.items():
            label = label.strip()
            if not label:
                error_list.append("Sonority level has an empty label")
                continue
            if label in sonority_inventory:
                error_list.append(f"Sonority '{label}' is already defined")
                continue

            sonority_def_result = SonorityDefinition.load(label, sonority_def_dict, inventory)
            if sonority_def_result.is_err():
                error_list.extend(sonority_def_result.unwrap_err())
                continue

            sonority_inventory[label] = sonority_def_result.unwrap()

        if error_list:
            return Err(error_list)

        inv = cls(sonority_inventory)
        inv._sort_by_specificity()
        check_result = inv.validate()
        if check_result.is_err():
            return Err(check_result.unwrap_err())

        return Ok(inv)

    def validate(self) -> Result[None, list[str]]:
        """Check for duplicate levels."""
        error_list = []

        seen_levels: dict[int, str] = {}
        for label, sonority_def in self.data.items():
            if sonority_def.level in seen_levels:
                error_list.append(
                    f"Sonority '{label}' and '{seen_levels[sonority_def.level]}' share level {sonority_def.level}"
                )
            seen_levels[sonority_def.level] = label

        if error_list:
            return Err(error_list)
        return Ok(None)

    def assign_sonority(self, segment: FeatureBundle) -> SonorityDefinition:
        """Match a segment against sonority definitions, most-specific-first.

        Args:
            segment: Feature bundle of the segment to classify.

        Returns:
            The matching SonorityDefinition.

        Raises:
            ValueError: If no sonority definition matches the segment.
        """
        for sonority_def in self._sorted:
            if sonority_def.bundle is None or segment.match_pattern(sonority_def.bundle):
                return sonority_def
        raise ValueError(f"No sonority definition matches segment {segment}")
