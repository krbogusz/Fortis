from collections import UserDict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from src.fortis.parsing import parse_feature_value
from src.fortis.general.file_handling import load_csv_file
from src.fortis.imports.features import FeatureInventory
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.result import Err, Ok, Result


@dataclass
class LetterDefinition:
    """A letter symbol with its symbol and feature bundle."""

    symbol: str
    bundle: FeatureBundle

    @classmethod
    def load(cls, row: dict[str, str], features: FeatureInventory) -> Result[LetterDefinition, list[str]]:
        """Load a letter definition from a dictionary."""
        error_list = []
        symbol = row.get("symbol", "").strip()
        if not symbol:
            return Err(["Letter is missing required field 'symbol'"])

        bundle = FeatureBundle()
        for feature_name, raw_value in row.items():
            if feature_name == "symbol":
                continue
            if feature_name not in features:
                error_list.append(f"Letter '{symbol}' has a feature '{feature_name}' that is unknown")
                continue
            raw_value = raw_value.strip()
            if not raw_value:
                continue  # empty cell = unspecified = omitted from bundle
            value_result = parse_feature_value(raw_value, feature_name, features)
            if value_result.is_err():
                error_list.append(value_result.unwrap_err())
                continue
            value = value_result.unwrap()
            if value.value is None:
                continue  # parsed as unspecified = omitted from bundle
            bundle[feature_name] = value

        if error_list:
            return Err(error_list)
        return Ok(LetterDefinition(symbol, bundle))


class LetterInventory(UserDict[str, LetterDefinition]):
    """Segment symbols mapped to their feature bundles.

    Pre-computes sorted symbol lists at construction time for greedy
    longest-first matching in IPA tokenisation.  Access them via the
    ``sorted_keys`` property.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialise the inventory and pre-compute sorted keys."""
        super().__init__(*args, **kwargs)
        self._sorted_keys: list[str] = sorted(self.keys(), key=len, reverse=True)

    @property
    def sorted_keys(self) -> list[str]:
        """Letter symbols sorted longest-first for greedy matching."""
        return self._sorted_keys

    @classmethod
    def load(cls, path: Path, features: FeatureInventory) -> Result[LetterInventory, list[str]]:
        """Load from a CSV file (columns = features, rows = symbols).

        Args:
            path: Path to the CSV file.
            features: Feature inventory for column validation and value parsing.
        """
        error_list = []

        data_result = load_csv_file(path)
        if data_result.is_err():
            return Err([data_result.unwrap_err()])
        rows = data_result.unwrap()

        # Validate column headers against feature inventory
        if rows:
            headers = set(rows[0].keys())
            for header in headers:
                if header != "symbol" and header not in features:
                    error_list.append(f"CSV column '{header}' is not a known feature")

        letter_inventory = {}
        for row in rows:
            letter_def_result = LetterDefinition.load(row, features)

            if letter_def_result.is_err():
                error_list.extend(letter_def_result.unwrap_err())
                continue

            letter_def = letter_def_result.unwrap()

            if letter_def.symbol in letter_inventory:
                error_list.append(f"Duplicate symbol '{letter_def.symbol}'")
            letter_inventory[letter_def.symbol] = letter_def

        if error_list:
            return Err(error_list)

        inv = cls(letter_inventory)
        check_result = inv.validate()
        if check_result.is_err():
            return Err(check_result.unwrap_err())

        return Ok(inv)

    def validate(self) -> Result[None, list[str]]:
        """Check for symbols with empty feature bundles or duplicate bundles."""
        error_list = []

        for symbol, letter_def in self.data.items():
            if not letter_def.bundle:
                error_list.append(f"Symbol '{symbol}' has no feature specifications")

        # Check for letters with identical feature bundles
        bundle_to_symbols: dict[tuple[tuple[str, int | tuple[int | None | str, ...] | str | None], ...], list[str]] = {}
        for symbol, letter_def in self.data.items():
            key = tuple(
                sorted(
                    (k, tuple(v) if isinstance(v, list) else v)
                    for k, value in letter_def.bundle.items()
                    for v in [value.value]
                )
            )
            bundle_to_symbols.setdefault(key, []).append(symbol)
        for symbols in bundle_to_symbols.values():
            if len(symbols) > 1:
                names = " and ".join(repr(s) for s in symbols)
                error_list.append(f"Letters {names} have identical feature bundles")

        if error_list:
            return Err(error_list)
        return Ok(None)