import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
nltk.download('punkt', quiet=True)
text = "The quick brown fox jumps over the lazy dog."
words = word_tokenize(text)
bigrams_list = list(ngrams(words, 2))
print(bigrams_list)
