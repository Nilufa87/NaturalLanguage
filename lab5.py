import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('wordnet', quiet=True)

lemmatizer = WordNetLemmatizer()
text = "The cats are running and jumping quickly."
words = word_tokenize(text)
lemmatized = [lemmatizer.lemmatize(w) for w in words]
print(lemmatized)
