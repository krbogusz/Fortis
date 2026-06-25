from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Paths:
    """Paths to various directories."""

    root: Path = Path(__file__).parent.parent.parent
    inventories: Path = root / "inventories"
    letters: Path = inventories / "letters.csv"
    rules: Path = inventories / "rules.toml"
    words: Path = inventories / "words.toml"


@dataclass
class ValueSymbols:
    """Text values."""

    present: set[str] = field(default_factory=lambda: {"+", "1", "present"})
    absent: set[str] = field(default_factory=lambda: {"-", "0", "absent"})
    unspecified: set[str] = field(default_factory=lambda: {"∅", "none", "unspecified"})


@dataclass
class Config:
    """Configuration."""

    paths: Paths = field(default_factory=Paths)
    value_symbols: ValueSymbols = field(default_factory=ValueSymbols)
    special_symbols: set[str] = field(default_factory=lambda: {"."})
    reserved_symbols: set[str] = field(
        default_factory=lambda: {"[", "]", "{", "}", ".", "#", "$", "<", ">", "!", "@", ";", ":"}
    )
    greek_alphabet: set[str] = field(
        default_factory=lambda: {
            "α",
            "β",
            "γ",
            "δ",
            "ε",
            "ζ",
            "η",
            "θ",
            "ι",
            "κ",
            "λ",
            "μ",
            "ν",
            "ξ",
            "ο",
            "π",
            "ρ",
            "σ",
            "ς",
            "τ",
            "υ",
            "φ",
            "χ",
            "ψ",
            "ω",
        }
    )


config = Config()
