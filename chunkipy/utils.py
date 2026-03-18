"""Shared utility helpers used across chunkipy internals and optional extras."""

import importlib
from typing import Iterable, List

INSTRUCTIONS = """
chunkipy error: missing {package_name}.

This feature requires additional dependencies:

    $ pip install chunkipy[{extra}] 
    
or 

    $ poetry add chunkipy[{extra}]

"""


def format_instructions(*, extra: str, package_name: str) -> str:
    """Build the installation hint shown when an optional dependency is missing."""
    return INSTRUCTIONS.format(extra=extra, package_name=package_name)


class MissingDependencyError(Exception):
    """Raised when an optional dependency required by an API is not installed."""
    pass


def import_dependencies(
    extra: str,
    package_name: str,
    attribute_names: Iterable[str] | None = None,
):
    """Import an optional dependency and optionally fetch named attributes.

    Args:
        extra: Name of the optional extra exposed by the package.
        package_name: Importable module name.
        attribute_names: Optional attribute names to resolve from the module.

    Returns:
        The imported module when ``attribute_names`` is empty, otherwise a list
        containing the module followed by the requested attributes.

    Raises:
        MissingDependencyError: If the module or any requested attribute cannot
            be imported.
    """
    attribute_names = list(attribute_names or [])
    module = None
    attributes = tuple(None for _ in attribute_names)
    try:
        module = importlib.import_module(package_name)
        attributes = tuple(getattr(module, name) for name in attribute_names)
    except (ImportError, AttributeError) as e:
        raise MissingDependencyError(
            format_instructions(package_name=package_name, extra=extra)
        ) from e
    imports = [module, *attributes] if attributes else module
    return imports