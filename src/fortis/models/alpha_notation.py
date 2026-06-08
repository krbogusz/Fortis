from enum import StrEnum, auto


class AlphaOperation(StrEnum):
    """Greek-variable notation; bind-vs-recall is resolved at match time."""

    same = auto()  # [alpha F]
    opposite = auto()  # [-alpha F] (binary/unary and simple only)
    other = auto()  # [!alpha F]
