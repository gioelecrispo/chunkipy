
from abc import ABC


class BaseSizeEstimator(ABC):
    """
    Base class for size estimators.
    """

    def estimate_size(self, text: str) -> int:
        """
        Estimate the size of the given text.

        Args:
            text (str): The text to estimate the size of.

        Returns:
            int: The estimated size of the text in bytes.
        """
        raise NotImplementedError("Subclasses must implement the estimate_size method.")