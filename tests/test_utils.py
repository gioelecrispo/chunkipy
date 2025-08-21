import unittest
import pytest
import types
from chunkipy import utils
import math
import math

class TestUtils(unittest.TestCase):
    def test_format_instructions(self):
        extra = "foo"
        package_name = "bar"
        result = utils.format_instructions(extra=extra, package_name=package_name)
        assert "missing bar" in result
        assert "pip install chunkipy[foo]" in result

    def test_import_dependencies_module_only(self):
        # Should import a standard library module successfully
        imports = utils.import_dependencies(extra="none", package_name="math")
        assert imports is math

    def test_import_dependencies_with_attributes(self):
        # Should import module and attributes
        imports = utils.import_dependencies(
            extra="none", package_name="math", attribute_names=["sqrt", "pi"]
        )
        assert imports[0] is math
        assert imports[1] is math.sqrt
        assert imports[2] == math.pi

    def test_import_dependencies_missing_module(self):
        with pytest.raises(utils.MissingDependencyError) as excinfo:
            utils.import_dependencies(extra="foo", package_name="nonexistent_module_xyz")
        assert "missing nonexistent_module_xyz" in str(excinfo.value)

    def test_import_dependencies_missing_attribute(self):
        # math module does not have attribute 'nonexistent_attr'
        with pytest.raises(utils.MissingDependencyError) as excinfo:
            utils.import_dependencies(
                extra="foo", package_name="math", attribute_names=["nonexistent_attr"]
            )
        assert "missing math" in str(excinfo.value)