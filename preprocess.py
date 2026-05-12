import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

nltk.download('punkt')


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text


def tokenize_text(text):
    return word_tokenize(text)


def generate_ngrams(tokens, n=2):
    return list(ngrams(tokens, n))