from collections import UserDict
from pathlib import Path

from src.fortis.general.file_handling import load_csv_file
from src.fortis.inventories.feature_inventory import FeatureInventory
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.feature_spec import FeatureSpec
from src.fortis.models.values import single_value_from_str
from src.fortis.result import Err, Ok, Result


class LetterInventory(UserDict[str, FeatureBundle]):
    """Segment symbols mapped to their feature bundles."""

    @classmethod
    def load(cls, path: Path, inventory: FeatureInventory) -> Result[LetterInventory, list[str]]:
        """Load from a CSV file (columns = features, rows = symbols).

        Args:
            path: Path to the CSV file.
            inventory: Feature inventory for column validation and value parsing.
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
                if header != "symbol" and header not in inventory:
                    error_list.append(f"CSV column '{header}' is not a known feature")

        letter_inventory: dict[str, FeatureBundle] = {}
        for row in rows:
            symbol = row.get("symbol", "").strip()
            if not symbol:
                error_list.append("Letter is missing required field 'symbol'")
                continue

            bundle = FeatureBundle()
            row_errors = False
            for feature_name, raw_value in row.items():
                if feature_name == "symbol":
                    continue
                if feature_name not in inventory:
                    continue  # already reported above
                raw_value = raw_value.strip()
                if not raw_value:
                    continue  # unspecified

                if ">" in raw_value:
                    contour: list[int | None] = []
                    for step in raw_value.split(">"):
                        step = step.strip()
                        if not step:
                            error_list.append(f"Empty contour step for '{feature_name}' in letter '{symbol}'")
                            row_errors = True
                            break
                        result = single_value_from_str(step, feature_name, inventory)
                        if result.is_err():
                            error_list.append(result.unwrap_err())
                            row_errors = True
                            break
                        contour.append(result.unwrap())
                    else:
                        bundle[feature_name] = FeatureSpec(feature_name, contour)
                else:
                    result = single_value_from_str(raw_value, feature_name, inventory)
                    if result.is_err():
                        error_list.append(result.unwrap_err())
                        row_errors = True
                        continue
                    value = result.unwrap()
                    if value is not None:
                        bundle[feature_name] = FeatureSpec(feature_name, value)

            if row_errors:
                continue

            if symbol in letter_inventory:
                error_list.append(f"Duplicate symbol '{symbol}'")
            letter_inventory[symbol] = bundle

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

        for symbol, bundle in self.data.items():
            if not bundle:
                error_list.append(f"Symbol '{symbol}' has no feature specifications")

        # Check for letters with identical feature bundles
        bundle_to_symbols: dict[tuple[tuple[str, int | tuple[int | None, ...] | None], ...], list[str]] = {}
        for symbol, bundle in self.data.items():
            key = tuple(
                sorted((k, tuple(spec.value) if isinstance(spec.value, list) else spec.value) for k, spec in bundle.items())
            )
            bundle_to_symbols.setdefault(key, []).append(symbol)
        for symbols in bundle_to_symbols.values():
            if len(symbols) > 1:
                names = " and ".join(repr(s) for s in symbols)
                error_list.append(f"Letters {names} have identical feature bundles")

        if error_list:
            return Err(error_list)
        return Ok(None)
