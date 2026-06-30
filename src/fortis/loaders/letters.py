from __future__ import annotations

from pathlib import Path

from src.fortis.general.file_handling import load_csv_file
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.features import FeatureInventory
from src.fortis.models.inventories import Letter, LetterInventory
from src.fortis.parsing.bundles import parse_feature_spec
from src.fortis.result import Err, Ok, Result


def load_letter(row: dict[str, str], features: FeatureInventory) -> Result[Letter, list[str]]:
    """Load a letter definition from a dictionary."""
    error_list = []
    symbol = row.get("symbol", "").strip()
    if not symbol:
        return Err(["A letter is missing the required 'symbol' field"])

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
        match parse_feature_spec(feature_name + raw_value, features):
            case Err(err):
                error_list.append(err)
                continue
            case Ok(spec):
                if spec.value is None:
                    continue  # parsed as unspecified = omitted from bundle
                bundle[feature_name] = spec

    if error_list:
        return Err(error_list)
    return Ok(Letter(symbol, bundle))


def load_letter_inventory(
    path: Path, features: FeatureInventory
) -> Result[LetterInventory, list[str]]:
    """Load from a CSV file (columns = features, rows = symbols).

    Args:
        path: Path to the CSV file.
        features: Feature inventory for column validation and value parsing.
    """
    error_list = []

    match load_csv_file(path):
        case Err(err):
            return Err([err])
        case Ok(result):
            rows = result

    # Validate column headers against feature inventory
    if rows:
        headers = set(rows[0].keys())
        for header in headers:
            if header != "symbol" and header not in features:
                error_list.append(f"CSV column '{header}' is not a known feature")

    letter_inventory = LetterInventory()
    for row in rows:
        match load_letter(row, features):
            case Err(err):
                error_list.extend(err)
                continue
            case Ok(result):
                letter_def = result
        if letter_def.symbol in letter_inventory:
            error_list.append(f"Duplicate symbol '{letter_def.symbol}'")
            continue
        letter_inventory[letter_def.symbol] = letter_def

    if error_list:
        return Err(error_list)

    return validate_letter_inventory(letter_inventory).map(lambda _: letter_inventory)


def validate_letter_inventory(letter_inventory: LetterInventory) -> Result[None, list[str]]:
    """Check for symbols with empty feature bundles or duplicate bundles."""
    error_list = []

    for symbol, letter_def in letter_inventory.data.items():
        if not letter_def.bundle:
            error_list.append(f"Symbol '{symbol}' has no feature specifications")

    # Check for letters with identical feature bundles
    bundle_to_symbols: dict[tuple[tuple[str, object], ...], list[str]] = {}
    for symbol, letter_def in letter_inventory.data.items():
        key = tuple(
            sorted(
                (k, tuple(v.value) if isinstance(v.value, tuple) else v.value)
                for k, v in letter_def.bundle.items()
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
