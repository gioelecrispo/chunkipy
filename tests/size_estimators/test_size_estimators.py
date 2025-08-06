# FILE: tests/size_estimators/test_size_estimators.py

import unittest
from chunkipy.size_estimators import CharSizeEstimator, WordSizeEstimator, OpenAISizeEstimator
from chunkipy.size_estimators.base_size_estimator import BaseSizeEstimator
from chunkipy.utils import MissingDependencyError

class TestCharSizeEstimator(unittest.TestCase):
    def test_estimate_size(self):
        estimator = CharSizeEstimator()
        text = "This is a test."
        self.assertEqual(estimator.estimate_size(text), len(text))

class TestWordSizeEstimator(unittest.TestCase):
    def test_estimate_size(self):
        estimator = WordSizeEstimator()
        text = "This is a test."
        self.assertEqual(estimator.estimate_size(text), 4)  # 4 words

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

class TestBaseSizeEstimator(unittest.TestCase):
    def test_abstract_method(self):
        class DummySizeEstimator(BaseSizeEstimator):
            pass

        with self.assertRaises(NotImplementedError):
            DummySizeEstimator().estimate_size("test")

if __name__ == "__main__":
    unittest.main()