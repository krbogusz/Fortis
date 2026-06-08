from collections import UserDict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from src.fortis.general.file_handling import load_toml_file
from src.fortis.general.utils import safe_int
from src.fortis.imports.features import FeatureInventory
from src.fortis.models.pattern_bundle import PatternBundle
from src.fortis.result import Err, Ok, Result


@dataclass
class SyllablePartDefinition:
    """A constraint definition for one syllable part (onset, nucleus, or coda).

    Args:
        part_type: Which part of the syllable ("onset", "nucleus", or "coda").
        time: Application time for this constraint.
        definition: Exact feature bundle for nucleus matching (nucleus only).
        required: Raw pattern string for required features (onset/coda only).
        forbidden: Raw pattern string for forbidden features (onset/coda only).
    """

    part_type: str
    time: int
    definition: PatternBundle | None = None
    required: str | None = None
    forbidden: str | None = None

    @classmethod
    def load(
        cls,
        part_type: str,
        time: int,
        part_dict: Any,
        features: FeatureInventory,
    ) -> Result[SyllablePartDefinition, list[str]]:
        """Build a SyllablePart from a raw TOML entry.

        Args:
            part_type: One of "onset", "nucleus", "coda".
            time: Application time (integer).
            part_dict: Raw dictionary from the TOML file.
            features: Feature inventory for bundle parsing.
        """
        error_list: list[str] = []

        valid_types = ("onset", "nucleus", "coda")
        if part_type not in valid_types:
            return Err([f"Invalid syllable part type '{part_type}' (expected {', '.join(valid_types)})"])

        if not isinstance(part_dict, dict):
            return Err([f"Syllable part '{part_type}' at time {time} must be a table"])

        definition: PatternBundle | None = None
        required: str | None = None
        forbidden: str | None = None

        if part_type == "nucleus":
            if "required" in part_dict or "forbidden" in part_dict:
                error_list.append(f"Nucleus at time {time} uses 'definition', not 'required' or 'forbidden'")
            defn_raw = part_dict.get("definition")
            if not defn_raw:
                error_list.append(f"Nucleus at time {time} is missing required field 'definition'")
            else:
                bundle_result = PatternBundle.from_string(str(defn_raw), features=features)
                if bundle_result.is_err():
                    error_list.extend(bundle_result.unwrap_err())
                else:
                    definition = bundle_result.unwrap()
        else:
            if "definition" in part_dict:
                error_list.append(
                    f"{part_type.capitalize()} at time {time} uses 'required'/'forbidden', not 'definition'"
                )
            req_raw = part_dict.get("required")
            if req_raw is not None:
                required = str(req_raw)
            forb_raw = part_dict.get("forbidden")
            if forb_raw is not None:
                forbidden = str(forb_raw)

        if error_list:
            return Err(error_list)

        return Ok(
            SyllablePartDefinition(
                part_type=part_type,
                time=time,
                definition=definition,
                required=required,
                forbidden=forbidden,
            )
        )


class SyllablePartsInventory(UserDict[int, dict[str, SyllablePartDefinition]]):
    """Syllable part constraints keyed by application time.

    Each time key maps to a dict of part_type → SyllablePart (e.g. "onset",
    "nucleus", "coda"). Dict keys enforce one of each part per time.
    """

    @classmethod
    def load(cls, path: Path, features: FeatureInventory) -> Result[SyllablePartsInventory, list[str]]:
        """Load syllable settings from a TOML file.

        Args:
            path: Path to the syllable parts TOML file.
            features: Feature inventory for bundle parsing.
        """
        error_list: list[str] = []

        data_result = load_toml_file(path)
        if data_result.is_err():
            return Err([data_result.unwrap_err()])
        data = data_result.unwrap()

        syllable_parts_inv: dict[int, dict[str, SyllablePartDefinition]] = {}

        for key, value in data.items():
            time_val = safe_int(key)
            if time_val is None:
                error_list.append(f"Syllable settings key '{key}' is not a valid integer time")
                continue

            if not isinstance(value, dict):
                error_list.append(f"Syllable settings at time {key} must be a table")
                continue

            parts_at_time: dict[str, SyllablePartDefinition] = {}

            for part_type, part_dict in value.items():
                part_type = part_type.strip().lower()
                if not isinstance(part_dict, dict):
                    error_list.append(f"Syllable part '{part_type}' at time {time_val} must be a table")
                    continue
                if part_type in parts_at_time:
                    error_list.append(f"Duplicate syllable part '{part_type}' at time {time_val}")
                    continue

                part_result = SyllablePartDefinition.load(part_type, time_val, part_dict, features)
                if part_result.is_err():
                    error_list.extend(part_result.unwrap_err())
                    continue

                parts_at_time[part_type] = part_result.unwrap()

            syllable_parts_inv[time_val] = parts_at_time

        if error_list:
            return Err(error_list)

        inv = cls(syllable_parts_inv)
        check_result = inv.validate()
        if check_result.is_err():
            return Err(check_result.unwrap_err())

        return Ok(inv)

    def validate(self) -> Result[None, list[str]]:
        """Check for cross-part consistency issues."""
        return Ok(None)

    def get_nucleus(self, time: int = 0) -> PatternBundle | None:
        """Get the nucleus definition bundle at the given time."""
        part = self.data.get(time, {}).get("nucleus")
        if part is not None and part.definition is not None:
            return part.definition
        return None

    def get_onset(self, time: int = 0) -> tuple[str | None, str | None]:
        """Get (required, forbidden) for onset at the given time."""
        part = self.data.get(time, {}).get("onset")
        if part is not None:
            return (part.required, part.forbidden)
        return (None, None)

    def get_coda(self, time: int = 0) -> tuple[str | None, str | None]:
        """Get (required, forbidden) for coda at the given time."""
        part = self.data.get(time, {}).get("coda")
        if part is not None:
            return (part.required, part.forbidden)
        return (None, None)
