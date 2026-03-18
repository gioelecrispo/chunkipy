import unittest

from chunkipy.size_estimators.base_size_estimator import BaseSizeEstimator


class TestBaseSizeEstimator(unittest.TestCase):
    def test_abstract_method(self):
        class DummySizeEstimator(BaseSizeEstimator):
            pass

        with self.assertRaises(TypeError):
            DummySizeEstimator()
