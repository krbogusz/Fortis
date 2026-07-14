from __future__ import annotations

from pathlib import Path

from src.fortis.config import config
from src.fortis.loaders.diacritics import load_diacritic_inventory
from src.fortis.loaders.features import load_feature_inventory
from src.fortis.loaders.letters import load_letter_inventory
from src.fortis.loaders.rules import load_rule_inventory
from src.fortis.loaders.settings import load_settings
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


def unfired_scoped_rules(rules: RuleInventory, words: WordInventory) -> list[tuple[str, str]]:
    """Word-scoped rules naming a word absent from the lexicon — ``(rule_id, word)`` pairs.

    A ``words`` entry matches a word by id, gloss or seed IPA; one that matches none makes the rule
    silently never fire, which is almost always a typo. Non-fatal — the project still loads —
    so it is returned rather than raised; the CLI and web app surface the list for the author.
    """
    known = set(words.keys()) | {w.gloss for w in words.values() if w.gloss} | {
        w.seed.ipa for w in words.values()
    }
    return [
        (rule.id, name)
        for rules_at_time in rules.values()
        for rule in rules_at_time
        for name in rule.words
        if name not in known
    ]


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

    def pick_dual(toml_name: str, csv_name: str) -> Path:
        """The path for a dual-format inventory (``.toml`` or ``.csv``).

        Returns the project's ``.toml`` if present, else its ``.csv``, else the shipped
        default's ``.toml``. Words, rules, diacritics, and sonorities each load from either
        format (their loaders dispatch by extension); TOML wins when both are present, so a
        project can carry a canonical ``.toml`` and a derived ``.csv`` side by side.
        """
        for filename in (toml_name, csv_name):
            candidate = project_dir / filename
            if candidate.exists():
                return candidate
        return defaults / toml_name

    if words_path is None:
        words_path = pick_dual("words.toml", "words.csv")
    if rules_path is None:
        rules_path = pick_dual("rules.toml", "rules.csv")
    diacritics_path = pick_dual("diacritics.toml", "diacritics.csv")
    sonorities_path = pick_dual("sonorities.toml", "sonorities.csv")

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
    match load_diacritic_inventory(diacritics_path, features):
        case Err(err):
            error_list.extend(f"{diacritics_path.name}: {e}" for e in err)
        case Ok(result):
            diacritics = result

    # ---- Sonorities ------------------------------------------------------------------------------
    sonorities: SonoritiesInventory | None = None
    match load_sonorities_inventory(sonorities_path, features):
        case Err(err):
            error_list.extend(f"{sonorities_path.name}: {e}" for e in err)
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
            error_list.extend(f"{words_path.name}: {e}" for e in err)
        case Ok(result):
            words = result

    # ---- Rules -----------------------------------------------------------------------------------
    rules: RuleInventory | None = None
    match load_rule_inventory(rules_path, features):
        case Err(err):
            error_list.extend(f"{rules_path.name}: {e}" for e in err)
        case Ok(result):
            rules = result

    # ---- Settings (optional tunable parameters) --------------------------------------------------
    # Absent ⇒ built-in defaults; present keys override. Not feature-dependent, so order-free.
    settings = None
    match load_settings(pick("settings.toml")):
        case Err(err):
            error_list.extend(f"settings.toml: {e}" for e in err)
        case Ok(result):
            settings = result

    if error_list:
        return Err(error_list)

    assert letters is not None
    assert diacritics is not None
    assert sonorities is not None
    assert syllable_parts is not None
    assert words is not None
    assert rules is not None
    assert settings is not None

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
            settings=settings,
        )
    )
