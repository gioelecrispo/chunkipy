from chunkipy.size_estimators.base_size_estimator import BaseSizeEstimator


class WordSizeEstimator(BaseSizeEstimator):
    """
    Size estimator that counts the number of words in the text.
    """

    def estimate_size(self, text: str) -> int:
        """
        Estimate the size of the given text by counting the number of words.

        Args:
            text (str): The text to estimate the size of.

        Returns:
            int: The estimated size of the text in words.
        """
        return len([t for t in text.split() if t != ' ' and t != '']) 