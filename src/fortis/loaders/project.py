from __future__ import annotations

import warnings
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


def _warn_unknown_scoped_words(rules: RuleInventory, words: WordInventory) -> None:
    """Warn when a word-scoped rule names a word absent from the lexicon (a likely typo).

    A ``words`` entry matches a word by ipa or gloss; one that matches neither makes the
    rule silently never fire, which is almost always a mistake. Non-fatal — the project
    still loads — so it is a warning, surfaced on stderr by the CLI.
    """
    known = set(words.keys()) | {word.gloss for word in words.values() if word.gloss is not None}
    for rules_at_time in rules.values():
        for rule in rules_at_time:
            for name in rule.words:
                if name not in known:
                    warnings.warn(
                        f"rule '{rule.id}': word-scope '{name}' matches no word "
                        "(by ipa or gloss) in words.toml — this rule will never fire",
                        stacklevel=2,
                    )


def load_project(
    project_dir: Path | None = None,
    *,
    words_path: Path | None = None,
    rules_path: Path | None = None,
) -> Result[Project, list[str]]:
    """Load every inventory and assemble a Project.

    A *project_dir* supplies only the files that differ from the shipped defaults
    (``config.paths.default``, i.e. ``projects/default``); any inventory file it omits
    falls back to the default. So a project that re-uses the default feature system
    needs no ``features.toml`` of its own. Features are loaded first since all other
    inventories depend on them.

    Args:
        project_dir: The project's directory — its files override the shipped defaults, and
            any it omits fall back to them. Defaults to ``projects/default`` itself.
        words_path: The lexicon file. Defaults to the project's ``words.toml`` (or the
            default's, if the project has none).
        rules_path: The sound-change file. Defaults likewise to ``rules.toml``.
    """
    defaults = config.paths.default
    if project_dir is None:
        project_dir = defaults

    def pick(filename: str) -> Path:
        """The project's copy of *filename* if it has one, else the shipped default."""
        candidate = project_dir / filename
        return candidate if candidate.exists() else defaults / filename

    if words_path is None:
        words_path = pick("words.toml")
    if rules_path is None:
        rules_path = pick("rules.toml")

    error_list: list[str] = []

    # ---- Features (no dependency) — required to proceed ------------------------------------------
    match load_feature_inventory(pick("features.toml")):
        case Err(err):
            return Err([f"features.toml: {e}" for e in err] if len(err) > 1 else err)
        case Ok(result):
            features = result

    # ---- Tiers (suprasegmental features + their policy) ------------------------------------------
    # Loaded before anything that references tone/stress: each tier registers its feature onto
    # `features`, so letters/diacritics/rules that mention them resolve. Absent ⇒ no tiers.
    tiers = TierInventory()
    tiers_path = pick("tiers.toml")
    if tiers_path.exists():
        match load_tier_inventory(tiers_path, features):
            case Err(err):
                error_list.extend(f"tiers.toml: {e}" for e in err)
            case Ok(result):
                tiers = result

    # ---- Letters ---------------------------------------------------------------------------------
    letters: LetterInventory | None = None
    match load_letter_inventory(pick("letters.csv"), features):
        case Err(err):
            error_list.extend(f"letters.csv: {e}" for e in err)
        case Ok(result):
            letters = result

    # ---- Diacritics ------------------------------------------------------------------------------
    diacritics: DiacriticInventory | None = None
    match load_diacritic_inventory(pick("diacritics.toml"), features):
        case Err(err):
            error_list.extend(f"diacritics.toml: {e}" for e in err)
        case Ok(result):
            diacritics = result

    # ---- Sonorities ------------------------------------------------------------------------------
    sonorities: SonoritiesInventory | None = None
    match load_sonorities_inventory(pick("sonorities.toml"), features):
        case Err(err):
            error_list.extend(f"sonorities.toml: {e}" for e in err)
        case Ok(result):
            sonorities = result

    # ---- Syllable parts --------------------------------------------------------------------------
    syllable_parts: SyllablePartsInventory | None = None
    match load_syllable_parts_inventory(pick("syllable_parts.toml"), features):
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

    if error_list:
        return Err(error_list)

    assert letters is not None
    assert diacritics is not None
    assert sonorities is not None
    assert syllable_parts is not None
    assert words is not None
    assert rules is not None

    _warn_unknown_scoped_words(rules, words)

    # The derivation starts at the earliest time defined by any time-keyed
    # inventory (rules, syllable parts). Untimed (None) rules are ignored here — they apply
    # last, not first. Falls back to 0 if nothing defines a time.
    time = min((t for t in (*rules.keys(), *syllable_parts.keys()) if t is not None), default=0)

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
