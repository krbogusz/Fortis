from collections import UserDict

from src.fortis.models.specs import PatternSpec, ResultSpec
from src.fortis.models.values import Value


class FeatureBundle(UserDict[str, Value]):
    """A collection of realized feature values, keyed by feature name.

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
