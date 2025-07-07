from chunkipy.size_estimators.base_size_estimator import BaseSizeEstimator


class CharSizeEstimator(BaseSizeEstimator):
    """
    Size estimator that counts the number of characters in the text.
    """

    def estimate_size(self, text: str) -> int:
        """
        Estimate the size of the given text by counting the number of characters.

        Args:
            text (str): The text to estimate the size of.

        Returns:
            int: The estimated size of the text in characters.
        """
        return len(text)