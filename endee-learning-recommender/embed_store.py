from sentence_transformers import SentenceTransformer
import endee

model = SentenceTransformer("all-MiniLM-L6-v2")

topics = open("data.txt").read().splitlines()

db = endee.Client()
collection = db.get_or_create_collection("learning_topics")

for i, topic in enumerate(topics):
    embedding = model.encode(topic).tolist()

    collection.add(
        ids=[str(i)],
        embeddings=[embedding],
        documents=[topic]
    )

print("✅ Data stored in Endee vector DB")
