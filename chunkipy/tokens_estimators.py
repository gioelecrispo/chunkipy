from abc import ABC, abstractmethod


class TokenEstimator(ABC):

    @abstractmethod
    def estimate_tokens(self, text):
        raise NotImplementedError()


class CharTokenEstimator(TokenEstimator):

    def estimate_tokens(self, text):
        return len(text)


class WordTokenEstimator(TokenEstimator):

    def estimate_tokens(self, text):
        return len([t for t in text.split(" ") if t != '' and ' '])