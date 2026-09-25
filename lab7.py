import nltk
#import string
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
nltk.download('punkt', quiet=True)

text = "NLP is fun. NLP is interesting. NLP helps in many applications."
words = word_tokenize(text)
"""words = [
    w for w in word_tokenize(text)
    if w not in string.punctuation
]"""
fdist = FreqDist(words)
print(fdist.most_common(5))
