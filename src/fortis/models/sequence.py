from collections import UserList

from src.fortis.models.feature_bundle import FeatureBundle


class Sequence(UserList[FeatureBundle]):
    """An ordered sequence of feature bundles (segments)."""
