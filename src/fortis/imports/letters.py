from collections import UserDict
from dataclasses import dataclass
from pathlib import Path

from src.fortis.general.file_handling import load_csv_file
from src.fortis.imports.features import FeatureInventory
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.feature_spec import FeatureSpec
from src.fortis.models.feature_value import FeatureValue
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
            raw_value = raw_value.strip() if raw_value is not None else ""
            if not raw_value:
                continue  # empty cell = feature not applicable, omit from bundle
            value_result = FeatureValue.from_str(raw_value, feature_name, features)

            if value_result.is_err():
                error_list.append(value_result.unwrap_err())
                continue
            value = value_result.unwrap()
            bundle[feature_name] = FeatureSpec(feature_name, value)

        if error_list:
            return Err(error_list)
        return Ok(LetterDefinition(symbol, bundle))


class LetterInventory(UserDict[str, LetterDefinition]):
    """Segment symbols mapped to their feature bundles."""

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
        bundle_to_symbols: dict[tuple[tuple[str, int | tuple[int | None, ...] | None], ...], list[str]] = {}
        for symbol, letter_def in self.data.items():
            key = tuple(
                sorted(
                    (k, tuple(v) if isinstance(v, list) else v)
                    for k, spec in letter_def.bundle.items()
                    for v in [spec.value.value]
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
