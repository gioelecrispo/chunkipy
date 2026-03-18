import unittest

from chunkipy.size_estimators import CharSizeEstimator, WordSizeEstimator


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
