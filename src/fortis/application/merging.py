"""Geometry-aware merge: apply a delta bundle to a base, delinking nodes.

When a delta sets a feature to ``None`` (unspecified), that feature and
all its descendants are removed from the result.  This is how diacritics
and rule results express "delink this node" — a value of ``None`` means
"unspecify", not "set to an abstract null".

``combine_with`` on ``FeatureBundle`` remains geometry-free (it cannot
take ``FeatureInventory`` without re-coupling models to the vocabulary).
"""

from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.features import FeatureInventory


def apply_bundle(
    base: FeatureBundle,
    delta: FeatureBundle,
    features: FeatureInventory,
    form_contours: bool = False,
) -> FeatureBundle:
    """Merge *delta* into *base* with geometry-aware delinking.

    1.  Merge: ``result = base.combine_with(delta, form_contours)``.
    2.  Delink pass: for every feature *f* in the merged result whose value
        is ``None``, drop *f*; and if *f* has children in the feature
        hierarchy, recursively drop all descendants of *f* as well.

    Args:
        base: The base feature bundle (e.g. a segment's features).
        delta: The delta feature bundle (e.g. a diacritic or rule result).
        features: Feature inventory providing the hierarchy (children/parent).
        form_contours: If True, overlapping features form contours instead
            of overriding.
    """
    merged = base.combine_with(delta, form_contours)

    # Delink pass: find all features set to None and remove them + descendants
    to_delink: list[str] = []
    for feature_name, value in merged.items():
        if value.value is None:
            to_delink.append(feature_name)

    # Recursively collect descendants
    delinked: set[str] = set()
    for feature_name in to_delink:
        _collect_descendants(feature_name, features, delinked)

    # Remove all delinked features
    for feature_name in delinked:
        if feature_name in merged:
            del merged[feature_name]

    return merged


def _collect_descendants(feature_name: str, features: FeatureInventory, result: set[str]) -> None:
    """Recursively collect a feature name and all its descendants."""
    result.add(feature_name)
    if feature_name in features:
        feature_def = features[feature_name]
        if feature_def.children:
            for child in feature_def.children:
                _collect_descendants(child, features, result)
