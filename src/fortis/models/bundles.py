from collections import UserDict

from src.fortis.models.specs import FeatureSpec, PatternSpec, ResultSpec


class FeatureBundle(UserDict[str, FeatureSpec]):
    """A collection of realized feature specifications, keyed by feature name.

    Used for concrete phonological material — segments in the lexicon,
    diacritics, letters, etc.
    """


class PatternBundle(UserDict[str, PatternSpec]):
    """A collection of pattern feature specifications, keyed by feature name.

    Used in rule target, context, and exception positions.
    """


class ResultBundle(UserDict[str, ResultSpec]):
    """A collection of result feature specifications, keyed by feature name.

    Used in rule result position.
    """
