"""Shared fixtures for the rule-induction tests.

These tests run against a small, fully **synthetic** benchmark project
(``tests/induction/fixtures/synth``) — never the mutable ``projects/`` data — so they stay
deterministic regardless of edits to any real project's lexicon. The fixture is self-consistent:
the hand cascade in its ``rules.toml`` regenerates every attested form with zero residual, and it
uses the same stage-time schema (``-200, -100, 750, 1000, 1200, 1400``) as the Latin benchmark.
The fixture is generated (see the header in its ``words.toml``), not hand-typed.
"""

from pathlib import Path

import pytest

from src.fortis.application.deriving import derive_all
from src.fortis.loaders.project import load_project
from src.fortis.models.derivation import Derivation
from src.fortis.models.project import Project

SYNTH_DIR = Path(__file__).parent / "fixtures" / "synth"


@pytest.fixture(scope="module")
def synth() -> Project:
    """The synthetic induction benchmark (input + stages + final), loaded from the fixture."""
    from src.fortis.analysis.accuracy import ingest_words

    project = load_project(SYNTH_DIR).unwrap()
    # segment the attested forms once; the shared words carry it to re-derivations
    ingest_words(project)
    return project


@pytest.fixture(scope="module")
def synth_derivations(synth: Project) -> list[Derivation]:
    """The synthetic lexicon derived once under its hand cascade (reused across tests)."""
    return derive_all(synth)
