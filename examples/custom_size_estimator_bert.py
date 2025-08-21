from chunkipy import TextChunker
from chunkipy.size_estimators import BaseSizeEstimator, WordSizeEstimator
from transformers import AutoTokenizer  # you need to install it separately


if __name__ == "__main__":

    with open("examples/texts/napoleon.txt", "r") as file:
        text = file.read()

    class BertSizeEstimator(BaseSizeEstimator):

        def __init__(self):
            self.bert_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

        def estimate_size(self, text):
            return len(self.bert_tokenizer.encode(text))


    word_size_estimator = WordSizeEstimator()
    bert_size_estimator = BertSizeEstimator()

    print(f"Num of chars: {len(text)}")
    print(f"Num of tokens (using WordSizeEstimator): {word_size_estimator.estimate_size(text)}")
    print(f"Num of tokens (using BertSizeEstimator): {bert_size_estimator.estimate_size(text)}")

    # Results:
    # Num of chars: 3149
    # Num of tokens (using WordSizeEstimator): 520
    # Num of tokens (using BertSizeEstimator): 603
    
    # set the tokens flag to False for chunking by chars
    text_chunker = TextChunker(512, size_estimator=bert_size_estimator)
    chunks = text_chunker.chunk(text)
    
    for i, chunk in enumerate(chunks):
        print(f"Chunk (i+1): {chunk}")