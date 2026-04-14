from sentence_transformers import SentenceTransformer
import endee

model = SentenceTransformer("all-MiniLM-L6-v2")

db = endee.Client()
collection = db.get_collection("learning_topics")


def search_topics(query):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    return results["documents"][0]
