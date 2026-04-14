from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("topics.index")
topics = open("topics.txt").read().splitlines()


def search_topics(query):
    query_vec = model.encode([query]).astype("float32")

    distances, indices = index.search(query_vec, 5)

    return [topics[i] for i in indices[0]]
