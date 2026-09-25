import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk
nltk.download('maxent_ne_chunker', quiet=True)
nltk.download('words', quiet=True)

text = "Barack Obama was born in Hawaii and worked at Microsoft."
words = word_tokenize(text)
pos_tags = pos_tag(words)
ner_tree = ne_chunk(pos_tags)
print(ner_tree)
