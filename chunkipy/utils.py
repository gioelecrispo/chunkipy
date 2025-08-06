import importlib
from typing import List

INSTRUCTIONS = """
chunkipy error: missing {package_name}.

This feature requires additional dependencies:

    $ pip install chunkipy [{extra}]

"""


def format_instructions(*, extra: str, package_name: str) -> str:
    return INSTRUCTIONS.format(extra=extra, package_name=package_name)


class MissingDependencyError(Exception):
    pass


def import_dependencies(extra: str, package_name: str, attribute_names: List[str] = []):
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