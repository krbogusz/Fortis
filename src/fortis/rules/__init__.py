"""Fortis rule engine — parse, match, and apply phonological rules.

This package implements the four-stage rule pipeline:

1. **Parse** — definition string → Rule AST (see :mod:`parsing`)
2. **Match** — recursive backtracking generator (see :mod:`match`)
3. **Locus finding** — find all positions where a rule applies (see :mod:`apply`)
4. **Rewrite** — instantiate result and splice into Sequence (see :mod:`apply`)

Typical usage::

    from src.fortis.inventories.inventories import Inventories
    from src.fortis.rules import apply_rules

    inv = Inventories.load()
    seq = string_to_sequence("bad", inv)
    result = apply_rules(seq, inv.rules.sorted_rules)
"""

from src.fortis.rules.apply import Locus, apply_rules, find_loci, rewrite
from src.fortis.rules.elements import (
    Application,
    Binding,
    Boundary,
    Bundle,
    Disjunction,
    Element,
    Env,
    Group,
    Null,
    Quantifier,
    Ref,
)
from src.fortis.rules.parsing import parse_rule_definition, parse_spe_definition
from src.fortis.rules.rule import Rule

__all__ = [
    # Elements
    "Application",
    "Binding",
    "Boundary",
    "Bundle",
    "Disjunction",
    "Element",
    "Env",
    "Group",
    "Null",
    "Quantifier",
    "Ref",
    # Rule
    "Rule",
    # Parsing
    "parse_rule_definition",
    "parse_spe_definition",
    # Application
    "Locus",
    "apply_rules",
    "find_loci",
    "rewrite",
]
