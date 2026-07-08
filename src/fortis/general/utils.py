from __future__ import annotations

import unicodedata
from collections import OrderedDict
from collections.abc import Callable, Hashable, Iterable
from typing import TypeVar

_V = TypeVar("_V")


class IdentityCache:
    """A small bounded LRU cache keyed by an object's identity, not its value.

    Meant for pure functions of an immutable-in-practice object (e.g. a ``Form``)
    that recurs as the same object across many consecutive calls — a rule sweep
    that keeps re-checking an unchanged form is the motivating case. Keying on
    ``id()`` alone would risk a false hit if that id gets reused for an unrelated,
    since-garbage-collected object; storing the original key alongside the value
    and verifying with ``is`` before returning it closes that hole. Bounded size
    keeps memory flat across a long-lived process instead of retaining every form
    ever seen.
    """

    def __init__(self, maxsize: int = 8) -> None:
        """Bound the cache to *maxsize* entries, evicting least-recently-used."""
        self._maxsize = maxsize
        self._data: OrderedDict[Hashable, tuple[object, object]] = OrderedDict()

    def get_or_compute(self, key_object: object, extra: Hashable, compute: Callable[[], _V]) -> _V:
        """*compute*'s result, cached by (identity of *key_object*, *extra*)."""
        cache_key = (id(key_object), extra)
        entry = self._data.get(cache_key)
        if entry is not None and entry[0] is key_object:
            self._data.move_to_end(cache_key)
            return entry[1]  # type: ignore[return-value]
        result = compute()
        self._data[cache_key] = (key_object, result)
        self._data.move_to_end(cache_key)
        if len(self._data) > self._maxsize:
            self._data.popitem(last=False)
        return result


def by_length(strings: Iterable[str]) -> list[str]:
    """Sort longest-first — the order greedy longest-match tokenisation needs."""
    return sorted(strings, key=len, reverse=True)


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
