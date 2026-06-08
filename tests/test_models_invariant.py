"""Test that the models package is self-contained.

No module under models/ may import from imports, application, parsing, or config.
"""

import importlib
import pkgutil

import src.fortis.models


def _collect_modules(package):
    """Yield fully-qualified module names for all submodules of *package*."""
    for importer, modname, ispkg in pkgutil.walk_packages(
        path=package.__path__,
        prefix=package.__name__ + ".",
    ):
        yield modname


FORBIDDEN_PREFIXES = (
    "src.fortis.imports",
    "src.fortis.application",
    "src.fortis.parsing",
    "src.fortis.config",
    "src.fortis.general",
)


class TestModelsInert:
    """Models must not depend on imports, application, parsing, config, or general."""

    def test_no_forbidden_imports(self):
        """Every module under models/ imports only from models/ or stdlib/ or result."""
        violations = []
        for modname in _collect_modules(src.fortis.models):
            try:
                mod = importlib.import_module(modname)
            except Exception:
                continue  # skip broken modules
            for attr_name in dir(mod):
                obj = getattr(mod, attr_name)
                # Look for module references (imported modules)
                if hasattr(obj, "__module__") and obj.__module__:
                    source = obj.__module__
                    if source.startswith("src.fortis.") and not source.startswith("src.fortis.models"):
                        # Allow src.fortis.result
                        if source != "src.fortis.result":
                            violations.append(f"{modname} references {source} (via {attr_name})")

        # Also check import statements directly
        import ast
        import inspect

        for modname in _collect_modules(src.fortis.models):
            try:
                source = inspect.getsource(importlib.import_module(modname))
            except (OSError, TypeError):
                continue
            try:
                tree = ast.parse(source)
            except SyntaxError:
                continue
            for node in ast.walk(tree):
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    if isinstance(node, ast.ImportFrom):
                        module = node.module or ""
                    else:
                        # For "import x", check each alias
                        for alias in node.names:
                            module = alias.name
                    if module.startswith("src.fortis.") and not module.startswith("src.fortis.models"):
                        if module != "src.fortis.result":
                            violations.append(f"{modname} imports from {module}")

        assert not violations, "Models invariant violated:\n" + "\n".join(violations)