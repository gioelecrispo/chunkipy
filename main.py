import logging
logging.basicConfig(level=logging.DEBUG)


from chunkipy import TextChunker, TokenEstimator, WordTokenEstimator
from transformers import AutoTokenizer  # you need to install it


if __name__ == "__main__":
    # Example 1
    print("*** Example 1: general usage ***")
    text = """Napoleon Bonaparte (born Napoleone Buonaparte; 15 August 1769 – 5 May 1821), later known by his regnal name Napoleon I, was a French military commander and political leader who rose to prominence during the French Revolution and led successful campaigns during the Revolutionary Wars. He was the de facto leader of the French Republic as First Consul from 1799 to 1804, then Emperor of the French from 1804 until 1814 and again in 1815. Napoleon's political and cultural legacy endures to this day, as a highly celebrated and controversial leader. He initiated many liberal reforms that have persisted in society, and is considered one of the greatest military commanders in history. His wars and campaigns are studied by militaries all over the world. Between three and six million civilians and soldiers perished in what became known as the Napoleonic Wars.
    Napoleon was born on the island of Corsica, not long after its annexation by France, to a native family descending from minor Italian nobility. He supported the French Revolution in 1789 while serving in the French army, and tried to spread its ideals to his native Corsica. He rose rapidly in the Army after he saved the governing French Directory by firing on royalist insurgents. In 1796, he began a military campaign against the Austrians and their Italian allies, scoring decisive victories and becoming a national hero. Two years later, he led a military expedition to Egypt that served as a springboard to political power. He engineered a coup in November 1799 and became First Consul of the Republic.
    Differences with the United Kingdom meant France faced the War of the Third Coalition by 1805. Napoleon shattered this coalition with victories in the Ulm campaign, and at the Battle of Austerlitz, which led to the dissolution of the Holy Roman Empire. In 1806, the Fourth Coalition took up arms against him. Napoleon defeated Prussia at the battles of Jena and Auerstedt, marched the Grande Armée into Eastern Europe, and defeated the Russians in June 1807 at Friedland, forcing the defeated nations of the Fourth Coalition to accept the Treaties of Tilsit. Two years later, the Austrians challenged the French again during the War of the Fifth Coalition, but Napoleon solidified his grip over Europe after triumphing at the Battle of Wagram.
    Hoping to extend the Continental System, his embargo against Britain, Napoleon invaded the Iberian Peninsula and declared his brother Joseph the King of Spain in 1808. The Spanish and the Portuguese revolted in the Peninsular War aided by a British army, culminating in defeat for Napoleon's marshals. Napoleon launched an invasion of Russia in the summer of 1812. The resulting campaign witnessed the catastrophic retreat of Napoleon's Grande Armée. In 1813, Prussia and Austria joined Russian forces in a Sixth Coalition against France, resulting in a large coalition army defeating Napoleon at the Battle of Leipzig. The coalition invaded France and captured Paris, forcing Napoleon to abdicate in April 1814. He was exiled to the island of Elba, between Corsica and Italy. In France, the Bourbons were restored to power."""

    class BertTokenEstimator(TokenEstimator):

        def __init__(self):
            self.bert_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

        def estimate_tokens(self, text):
            return len(self.bert_tokenizer.encode(text))

    word_token_estimator = WordTokenEstimator()
    bert_token_estimator = BertTokenEstimator()

    print(f"Num of chars: {len(text)}")
    print(f"Num of tokens (using WordTokenEstimator): {word_token_estimator.estimate_tokens(text)}")
    print(f"Num of tokens (using BertTokenEstimator): {bert_token_estimator.estimate_tokens(text)}")

    # Results:
    # Num of chars: 3149
    # Num of tokens (using WordTokenEstimator): 520
    # Num of tokens (using BertTokenEstimator): 603

    # set the tokens flag to False for chunkizing by chars
    text_chunker = TextChunker(512, tokens=True, token_estimator=bert_token_estimator)
    chunks = text_chunker.chunk(text)
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}, num of tokens: {bert_token_estimator.estimate_tokens(chunk)} -> {chunk}")

    # Example 2
    print("\n\n*** Example 2: overlapping ***")
    text_chunker = TextChunker(50, tokens=True, overlap_percent=0.3)

    # Set up test input
    text = "In this unit test, we are evaluating the overlapping functionality." \
           "This is a feature of the TextChunker class, which is important for a proper context keeping. The " \
           "goal is to ensure that overlapping chunks are generated correctly. For this purpose, we have chosen a " \
           "long text that exceeds 100 tokens. By setting the overlap_percent to 0.3, we expect the " \
           "generated chunks to have an overlap of approximately 30%. This will help us verify the effectiveness " \
           "of the overlapping feature. The TextChunker class should be able to handle this scenario and " \
           "produce the expected results. Let's proceed with running the test and asserting the generated chunks " \
           "for proper overlap. "

    # Generate chunks with overlapping
    chunks = text_chunker.chunk(text)

    # Print the resulting chunks
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}: {chunk}")

    # Example 3
    print("\n\n*** Example 3: custom split strategy ***")
    def split_by_arrow(text):
        return [t for t in text.split("->") if t != '' and ' ']

    text = "This is a tokenized text -> with custom split strategy."

    # Create a TextChunkizer object with custom split strategy
    text_chunker = TextChunker(chunk_size=8, tokens=True, split_strategies=[split_by_arrow])
    chunks = text_chunker.chunk(text)

    # Print the resulting chunks
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}: {chunk}")
