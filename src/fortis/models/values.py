"""Feature values: a single value, a contour, or their union."""

type AlphaValue = str  # Greek letter used as a variable name (e.g. "α", "β")
type SingleValue = int | None  # None == undefined / unspecified
type ContourValue = tuple[SingleValue, ...]  # ordered limbs; None per-limb allowed
type Value = SingleValue | ContourValue
type ContourPosition = str | tuple[int, ...]  # "initial", "final", "any", "all", or explicit positions


def make_value(limbs: list[SingleValue]) -> Value:
    """Build a feature value, collapsing a length-1 contour to a scalar.

    Args:
        limbs: Parsed limbs in order. A single limb is treated as a scalar.

    Returns:
        A ``SingleValue`` for one limb, otherwise a ``ContourValue``.
    """
    return limbs[0] if len(limbs) == 1 else tuple(limbs)
