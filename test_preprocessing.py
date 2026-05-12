from preprocess import *

text = "Wheat requires proper irrigation and fertilizer."

cleaned = clean_text(text)
print("Cleaned Text:")
print(cleaned)

print("\nTokens:")
tokens = tokenize_text(cleaned)
print(tokens)

print("\nBigrams:")
bigrams = generate_ngrams(tokens, 2)
print(bigrams)