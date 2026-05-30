from dataclasses import dataclass
from pathlib import Path

from src.fortis.general.file_handling import load_toml_file
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.feature_inventory import FeatureInventory
from src.fortis.result import Err, Ok, Result


@dataclass
class SyllableSettings:
    """Syllable settings."""

    nucleus: FeatureBundle

    @classmethod
    def load(cls, path: Path, inventory: FeatureInventory) -> Result[SyllableSettings, list[str]]:
        """Build syllable settings."""
        error_list = []

        data_result = load_toml_file(path)
        if data_result.is_err():
            return Err([data_result.unwrap_err()])
        data = data_result.unwrap()

        nucleus_raw = data.get("nucleus")
        if not nucleus_raw:
            error_list.append("No nucleus data")

        nucleus_bundle = FeatureBundle.from_str(str(nucleus_raw), inventory=inventory)
        if nucleus_bundle.is_err():
            error_list.extend(nucleus_bundle.unwrap_err())

        if error_list:
            return Err(error_list)
        else:
            return Ok(
                SyllableSettings(
                    nucleus_bundle.unwrap(),
                )
            )

    # —— Loading helpers ——————————————————————————————————————————————————————————————————————————
    @staticmethod
    def _load_level(label: str, sonority_def_dict: dict) -> Result[int, str]:
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
