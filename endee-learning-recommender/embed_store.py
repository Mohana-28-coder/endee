from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

topics = open("data.txt").read().splitlines()

embeddings = model.encode(topics)
embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

faiss.write_index(index, "topics.index")

with open("topics.txt", "w") as f:
    for t in topics:
        f.write(t + "\n")

print("✅ FAISS DB created")
