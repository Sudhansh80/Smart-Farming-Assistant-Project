from embedding import *

sentences = [
    "Wheat requires water",
    "Rice farming uses irrigation"
]

embeddings = generate_embedding(sentences)

similarity = calculate_similarity(
    embeddings[0],
    embeddings[1]
)

print("Cosine Similarity:")
print(similarity)