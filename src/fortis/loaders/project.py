from __future__ import annotations

from pathlib import Path

from src.fortis.config import config
from src.fortis.loaders.diacritics import load_diacritic_inventory
from src.fortis.loaders.features import load_feature_inventory
from src.fortis.loaders.letters import load_letter_inventory
from src.fortis.loaders.rules import load_rule_inventory
from src.fortis.loaders.sonorities import load_sonorities_inventory
from src.fortis.loaders.syllable_parts import load_syllable_parts_inventory
from src.fortis.loaders.tiers import load_tier_inventory
from src.fortis.loaders.words import load_word_inventory
from src.fortis.models.inventories import (
    DiacriticInventory,
    LetterInventory,
    SonoritiesInventory,
    SyllablePartsInventory,
    WordInventory,
)
from src.fortis.models.project import Project
from src.fortis.models.rules import RuleInventory
from src.fortis.models.tier_declaration import TierInventory
from src.fortis.result import Err, Ok, Result


def load_project(
    inventories_dir: Path | None = None,
    *,
    words_path: Path | None = None,
    rules_path: Path | None = None,
) -> Result[Project, list[str]]:
    """Load every inventory and assemble a Project.

    Features are loaded first since all other inventories depend on them.
    Words are loaded independently (no feature dependency).

    Args:
        inventories_dir: Directory containing the TOML/CSV data files.
            Defaults to ``config.paths.inventories``.
        words_path: The lexicon file. Defaults to ``inventories_dir/words.toml`` — so the
            words can be overridden while the rest of the inventories stay the defaults.
        rules_path: The sound-change file. Defaults to ``inventories_dir/rules.toml``.
    """
    if inventories_dir is None:
        inventories_dir = config.paths.inventories
    if words_path is None:
        words_path = inventories_dir / "words.toml"
    if rules_path is None:
        rules_path = inventories_dir / "rules.toml"

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
    sonorities: SonoritiesInventory | None = None
    match load_sonorities_inventory(inventories_dir / "sonorities.toml", features):
        case Err(err):
            error_list.extend(f"sonorities.toml: {e}" for e in err)
        case Ok(result):
            sonorities = result

    # ---- Syllable parts --------------------------------------------------------------------------
    syllable_parts: SyllablePartsInventory | None = None
    match load_syllable_parts_inventory(inventories_dir / "syllable_parts.toml", features):
        case Err(err):
            error_list.extend(f"syllable_parts.toml: {e}" for e in err)
        case Ok(result):
            syllable_parts = result

    # ---- Words -----------------------------------------------------------------------------------
    words: WordInventory | None = None
    match load_word_inventory(words_path):
        case Err(err):
            error_list.extend(f"words.toml: {e}" for e in err)
        case Ok(result):
            words = result

    # ---- Rules -----------------------------------------------------------------------------------
    rules: RuleInventory | None = None
    match load_rule_inventory(rules_path, features):
        case Err(err):
            error_list.extend(f"rules.toml: {e}" for e in err)
        case Ok(result):
            rules = result

    # ---- Tiers (optional: an absent tiers.toml ⇒ no autosegmental tiers) -------------------------
    tiers = TierInventory()
    tiers_path = inventories_dir / "tiers.toml"
    if tiers_path.exists():
        match load_tier_inventory(tiers_path, features):
            case Err(err):
                error_list.extend(f"tiers.toml: {e}" for e in err)
            case Ok(result):
                tiers = result

    if error_list:
        return Err(error_list)

    assert letters is not None
    assert diacritics is not None
    assert sonorities is not None
    assert syllable_parts is not None
    assert words is not None
    assert rules is not None

    # The derivation starts at the earliest time defined by any time-keyed
    # inventory (rules, syllable parts). Falls back to 0 if none define a time.
    time = min((*rules.keys(), *syllable_parts.keys()), default=0)

    return Ok(
        Project(
            features=features,
            letters=letters,
            diacritics=diacritics,
            sonorities=sonorities,
            syllable_parts=syllable_parts,
            words=words,
            rules=rules,
            time=time,
            tiers=tiers,
        )
    )
