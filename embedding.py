from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')


def generate_embedding(texts):
    return model.encode(texts)



def calculate_similarity(vec1, vec2):
    similarity = cosine_similarity([vec1], [vec2])
    return similarity[0][0]