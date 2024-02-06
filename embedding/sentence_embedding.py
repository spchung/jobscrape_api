from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")

def gen_embedding(text):
    return list(model.encode(text))