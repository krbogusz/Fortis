from __future__ import annotations

import unicodedata


def safe_int(input: str) -> int | None:
    """Convert a string to an int if it can be parsed as one.

    Returns an int on success or None if it cannot.
    """
    try:
        return int(input)
    except Exception:
        return None


def is_combining(ch: str) -> bool:
    """Return True if `ch` is a combining mark (nonspacing, spacing, or enclosing)."""
    return unicodedata.category(ch).startswith("M")
