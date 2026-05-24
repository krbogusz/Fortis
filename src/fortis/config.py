from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Paths:
    """Paths to various directories."""

    root: Path = Path(__file__).parent.parent.parent
    inventories: Path = root / "inventories"
    letters: Path = inventories / "letters.csv"


@dataclass
class Values:
    """Text values."""

    present: set[str] = field(default_factory=lambda: {"+", "1", "present"})
    absent: set[str] = field(default_factory=lambda: {"-", "0", "absent"})
    unspecified: set[str] = field(default_factory=lambda: {"", "∅", "none", "null", "unspecified"})


@dataclass
class Config:
    """Configuration."""

    paths: Paths = field(default_factory=Paths)
    values: Values = field(default_factory=Values)


config = Config()
