from pathlib import Path

from src.fortis.config import config
from src.fortis.loaders.diacritics import load_diacritic_inventory
from src.fortis.loaders.features import load_feature_inventory
from src.fortis.loaders.letters import load_letter_inventory
from src.fortis.loaders.sonorities import load_sonority_inventory
from src.fortis.loaders.syllable_parts import load_syllable_parts_inventory
from src.fortis.loaders.words import load_word_inventory
from src.fortis.models.inventories import (
    DiacriticInventory,
    LetterInventory,
    SonorityInventory,
    SyllablePartsInventory,
    WordInventory,
)
from src.fortis.models.project import Project
from src.fortis.models.rules import RuleInventory
from src.fortis.result import Err, Ok, Result


def load_project(inventories_dir: Path | None = None) -> Result[Project, list[str]]:
    """Load every inventory and assemble a Project.

    Features are loaded first since all other inventories depend on them.
    Words are loaded independently (no feature dependency).

    Args:
        inventories_dir: Directory containing the TOML/CSV data files.
            Defaults to ``config.paths.inventories``.
    """
    if inventories_dir is None:
        inventories_dir = config.paths.inventories

    error_list: list[str] = []

    # ---- Features (no dependency) — required to proceed ------------------------------------------
    match load_feature_inventory(inventories_dir / "features.toml"):
        case Err(err):
            return Err([f"features.toml: {e}" for e in err] if len(err) > 1 else err)
        case Ok(result):
            features = result

    # ---- Letters ---------------------------------------------------------------------------------
    letters: LetterInventory | None = None
    match load_letter_inventory(inventories_dir / "letters.csv", features):
        case Err(err):
            error_list.extend(f"letters.csv: {e}" for e in err)
        case Ok(result):
            letters = result

    # ---- Diacritics ------------------------------------------------------------------------------
    diacritics: DiacriticInventory | None = None
    match load_diacritic_inventory(inventories_dir / "diacritics.toml", features):
        case Err(err):
            error_list.extend(f"diacritics.toml: {e}" for e in err)
        case Ok(result):
            diacritics = result

    # ---- Sonorities ------------------------------------------------------------------------------
    sonority: SonorityInventory | None = None
    match load_sonority_inventory(inventories_dir / "sonorities.toml", features):
        case Err(err):
            error_list.extend(f"sonorities.toml: {e}" for e in err)
        case Ok(result):
            sonority = result

    # ---- Syllable parts --------------------------------------------------------------------------
    syllable_parts: SyllablePartsInventory | None = None
    match load_syllable_parts_inventory(inventories_dir / "syllable_parts.toml", features):
        case Err(err):
            error_list.extend(f"syllable_parts.toml: {e}" for e in err)
        case Ok(result):
            syllable_parts = result

    # ---- Words -----------------------------------------------------------------------------------
    words: WordInventory | None = None
    match load_word_inventory(inventories_dir / "words.toml"):
        case Err(err):
            error_list.extend(f"words.toml: {e}" for e in err)
        case Ok(result):
            words = result

    if error_list:
        return Err(error_list)

    assert letters is not None
    assert diacritics is not None
    assert sonority is not None
    assert syllable_parts is not None
    assert words is not None

    # TODO: load rules once the rules loader exists
    rules = RuleInventory()
    return Ok(
        Project(
            features=features,
            letters=letters,
            diacritics=diacritics,
            sonority=sonority,
            syllable_parts=syllable_parts,
            words=words,
            rules=rules,
        )
    )
