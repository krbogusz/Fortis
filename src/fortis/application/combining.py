"""Bundle algebra: combine, compare, and merge realized feature bundles.

Two layers, both pure functions over ``FeatureBundle`` data:

* ``combine`` / ``matches_exactly`` / ``differing`` are **geometry-free** — they
  consult no feature hierarchy, only the bundles themselves.
* ``merge`` is **geometry-aware** — it is ``combine`` followed by a delink pass
  that, for every feature unspecified to ``None``, drops that feature and all of
  its hierarchy descendants (a node going unspecified unspecifies its subtree).
  This is how diacritics and rule results express "delink this node".

(These were once two modules: ``combine`` lived as a method on the
``FeatureBundle`` model, which could not import ``FeatureInventory``, so the
geometry-aware half was split off. Now that both are application-layer functions
that may depend on the vocabulary, they belong together.)
"""
from __future__ import annotations

from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.features import FeatureInventory, FeatureKind
from src.fortis.models.specs import FeatureSpec
from src.fortis.models.values import form_contour


def combine(
    base: FeatureBundle, other: FeatureBundle, form_contours: bool = False
) -> FeatureBundle:
    """Combine *base* with *other*, returning a new bundle (geometry-free).

    Features in only one bundle are carried over. For a feature in both,
    *other* overrides — unless ``form_contours`` is set, in which case the two
    values form a contour (base's value followed by other's).

    Args:
        base: The bundle to start from (never mutated).
        other: The bundle to merge in.
        form_contours: If True, overlapping features form contours instead of
            overriding.
    """
    result = FeatureBundle(dict(base.data))
    for feature, spec in other.items():
        if feature in result and form_contours:
            combined = form_contour(result[feature].value, spec.value)
            result[feature] = FeatureSpec(feature=feature, value=combined)
        else:
            result[feature] = spec
    return result


def merge(
    base: FeatureBundle,
    delta: FeatureBundle,
    features: FeatureInventory,
    form_contours: bool = False,
) -> FeatureBundle:
    """Merge *delta* into *base* with geometry-aware delinking.

    First ``combine`` the two bundles; then, for every feature whose merged
    value is ``None`` (unspecified), drop that feature together with all of its
    descendants in the feature hierarchy. Unspecifying a node thus unlinks its
    whole subtree, even where the subtree carried concrete values in *base*.

    Args:
        base: The base bundle (e.g. a segment's features); never mutated.
        delta: The delta bundle (e.g. a rule result or diacritic).
        features: Feature inventory providing the hierarchy.
        form_contours: Passed through to ``combine``.
    """
    merged = combine(base, delta, form_contours)
    # Downward: unspecifying a node (value None) unlinks the node and its whole subtree.
    to_drop: set[str] = set()
    for feature, spec in merged.items():
        if spec.value is None:
            to_drop.add(feature)
            to_drop.update(features.descendants(feature))
    for feature in to_drop:
        merged.pop(feature, None)
    # Upward: a feature the *delta* sets implies its ancestor nodes — +rounded makes
    # the segment +labial (and +oral …), the mirror of the downward delink. Scoped to
    # the delta: a well-formed base already carries its ancestors, so completing only
    # what this merge introduces keeps the pass from masking a pre-existing orphan.
    # Only unary class nodes have an unambiguous "present" value (1). A non-unary
    # ancestor (a scalar/binary node carrying children) holds a value we cannot infer
    # from a daughter being set, so we leave it rather than fabricate one.
    for feature in delta:
        if feature in merged:  # the delta set a value here (not delinked away)
            for ancestor in features.ancestors(feature):
                if (
                    ancestor not in merged
                    and features[ancestor].kind == FeatureKind.unary
                    and features.parent(ancestor) is not None  # never the root (always implied)
                ):
                    merged[ancestor] = FeatureSpec(feature=ancestor, value=1)
    return merged


def matches_exactly(bundle: FeatureBundle, other: FeatureBundle) -> bool:
    """Whether *bundle* has the same features and values as *other*."""
    if set(bundle.data) != set(other.data):
        return False
    return all(bundle.data[f].value == other.data[f].value for f in bundle.data)


def differing(bundle: FeatureBundle, other: FeatureBundle) -> list[str]:
    """Return the features whose presence or value differs between the bundles."""
    diffs: list[str] = []
    for feature, spec in bundle.data.items():
        if feature not in other.data or other.data[feature].value != spec.value:
            diffs.append(feature)
    for feature in other.data:
        if feature not in bundle.data:
            diffs.append(feature)
    return diffs
