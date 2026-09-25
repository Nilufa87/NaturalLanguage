import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('punkt', quiet=True)
ps = PorterStemmer()
text = "The cats are running and jumping quickly."
words = word_tokenize(text)
stemmed = [ps.stem(w) for w in words]
print(stemmed)
