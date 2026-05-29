from collections import UserDict

from src.fortis.models.feature_inventory import FeatureInventory
from src.fortis.models.feature_spec import FeatureSpec, Place
from src.fortis.models.tiers import Tier
from src.fortis.models.values import present_value
from src.fortis.result import Err, Ok, Result


class FeatureBundle(UserDict[str, FeatureSpec]):
    """A collection of feature specifications, keyed by feature name."""

    def __init__(self, *args, inventory: FeatureInventory | None = None, **kwargs):
        """Init with a reference to inventory."""
        super().__init__(*args, **kwargs)
        self._inventory = inventory

    def __repr__(self) -> str:
        """Represent a feature bundle."""
        parts: list[str] = []
        for name, spec in self.data.items():
            value = spec.value
            if value is None:
                parts.append(f"{name}: ∅")
            elif isinstance(value, list):
                vals = ">".join(present_value(v) for v in value)
                parts.append(f"{name}: {vals}")
            elif self._inventory and name in self._inventory:
                ft_def = self._inventory[name]
                if ft_def.type in ("unary", "binary"):
                    parts.append(f"{name}: {present_value(value)}")
                else:
                    label = ft_def.values.get(value, str(value))
                    parts.append(f"{name}: {label}")
            elif value in (0, 1):
                parts.append(f"{name}: {present_value(value)}")
            else:
                parts.append(f"{name}: {value}")
        return "{" + ", ".join(parts) + "}"

    @classmethod
    def from_str(
        cls, raw_string: str, inventory: FeatureInventory, bare_unary_means_present: bool = False
    ) -> Result[FeatureBundle, list[str]]:
        """Parse a comma-separated feature bundle string (e.g. '+syll, -cons, height:2').

        Args:
            raw_string: Comma- or semicolon-separated feature specs.
            inventory: Feature inventory for name/value resolution.
            bare_unary_means_present: If True, a bare feature name on a unary
                feature is interpreted as present (value 1).
        """
        error_list = []
        string = raw_string.replace(" ", "").replace(";", ",")
        tokens = [t for t in string.split(",") if t]

        bundle = cls(inventory=inventory)
        for token in tokens:
            result = FeatureSpec.from_string(token, inventory, bare_unary_means_present)
            if result.is_err():
                error_list.append(result.unwrap_err())
                continue
            spec = result.unwrap()
            bundle[spec.feature] = spec

        if error_list:
            return Err(error_list)

        return Ok(bundle)

    def matches(self, other: FeatureBundle, ignore_none: bool = False, place: Place = "any") -> bool:
        """Check if every feature in this bundle matches the corresponding feature in *other*.

        Features present in *other* but not in *self* are unconstrained (the pattern
        doesn't care about them). Features present in *self* but not in *other* are
        treated as unspecified values.

        Args:
            other: The target bundle to match against.
            ignore_none: Treat missing features and None values as wildcards.
            place: Positional control for contour matching, passed to FeatureSpec.matches.
        """
        for feature, spec in self.data.items():
            if feature not in other.data:
                # Feature not present in target — unspecified
                if ignore_none:
                    continue
                return False
            if not spec.matches(other.data[feature], ignore_none=ignore_none, place=place):
                return False
        return True

    def present(self, inventory: FeatureInventory) -> str:
        """Format this bundle as a boxed display string.

        Binary/unary features show as ``+name`` or ``-name`` (using short names).
        Scalar features show as ``name: label``.
        Contour values show as ``name: label>label>...``.

        Args:
            inventory: Feature inventory for name/type/value lookups.
        """
        return "\n".join(self.present_lines(inventory))

    def present_lines(self, inventory: FeatureInventory) -> list[str]:
        """Return the boxed lines for this bundle (for side-by-side display).

        Args:
            inventory: Feature inventory for name/type/value lookups.
        """
        lines: list[str] = []
        has_syllable = False
        for feature_name in inventory:
            if feature_name not in self.data:
                continue
            ft_def = inventory[feature_name]
            if ft_def.tier == Tier.syllable and not has_syllable:
                lines.append("---")
                has_syllable = True
            short = ft_def.short
            spec = self.data[feature_name]
            if ft_def.type == "unary":
                lines.append(short)
            elif ft_def.type == "binary":
                if isinstance(spec.value, list):
                    vals = ">".join(present_value(v) for v in spec.value)
                    lines.append(f"{short}: {vals}")
                else:
                    lines.append(f"{short}: {present_value(spec.value)}")
            elif ft_def.type == "scalar":
                if isinstance(spec.value, list):
                    vals = ">".join(present_value(v) for v in spec.value)
                    lines.append(f"{short}: {vals}")
                else:
                    lines.append(f"{short}: {spec.value if spec.value is not None else '∅'}")

        if not lines:
            return ["⎡⎤"]

        width = max(len(line) for line in lines)
        result = [f"⎡{lines[0]:<{width}}⎤"]
        if len(lines) > 1:
            result.extend(f"⎢{line:<{width}}⎥" for line in lines[1:-1])
            result.append(f"⎣{lines[-1]:<{width}}⎦")

        return result

    def combine_with(self, other: FeatureBundle, form_contours: bool = False) -> FeatureBundle:
        """Combine this feature bundle with another.

        Args:
            other: The bundle to merge in.
            form_contours: If True, overlapping features form contours instead of overriding.
        """
        inventory = self._inventory or other._inventory
        result = FeatureBundle(dict(self.data), inventory=inventory)
        for feature_name, feature_spec in other.items():
            if feature_name not in result:
                result[feature_name] = feature_spec
            elif form_contours:
                result[feature_name] = result[feature_name].form_contour(feature_spec)
            else:
                result[feature_name] = feature_spec

        return result
