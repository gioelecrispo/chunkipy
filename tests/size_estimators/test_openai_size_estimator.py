import unittest

from chunkipy.size_estimators import OpenAISizeEstimator
from chunkipy.utils import MissingDependencyError


class TestOpenAISizeEstimator(unittest.TestCase):
    def test_estimate_size(self):
        try:
            estimator = OpenAISizeEstimator()
            text = "This is a test."
            size = estimator.estimate_size(text)
            self.assertIsInstance(size, int)
            self.assertGreater(size, 0)
        except MissingDependencyError:
            self.skipTest("tiktoken dependencies are not installed.")
