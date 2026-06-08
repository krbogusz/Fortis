from dataclasses import dataclass

from src.fortis.imports.features import FeatureInventory
from src.fortis.models.feature_value import FeatureValue
from src.fortis.result import Err, Ok, Result


@dataclass
class FeatureSpec:
    """A feature name paired with its value in a realized segment.

    No negation or position — those belong in PatternSpec.

    Args:
        feature: Full feature name.
        value: The feature's value.
    """

    feature: str
    value: FeatureValue

    def __repr__(self) -> str:
        """Repr for feature spec."""
        return f"{self.feature}: {self.value}"

    @classmethod
    def from_str(cls, raw_string: str, features: FeatureInventory) -> Result[FeatureSpec, str]:
        """Parse from a string like '+nasal', 'height:2', or 'glottal_aperture:spread'.

        Matches feature names longest-first (full names, then short names).

        Args:
            raw_string: The raw token to parse.
            features: Feature inventory for name/value resolution.
        """
        raw_string = raw_string.replace(" ", "")

        # Identify feature name via greedy longest-first matching
        feature_result = features.identify_feature(raw_string)
        if feature_result.is_err():
            return Err(feature_result.unwrap_err())
        feature = feature_result.unwrap()

        # Feature value
        match FeatureValue.from_str(raw_string, feature, features):
            case Ok(value):
                return Ok(FeatureSpec(feature, value))
            case Err() as err:
                return err
