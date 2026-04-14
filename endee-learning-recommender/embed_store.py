from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

topics = open("data.txt").read().splitlines()

# Create embeddings
embeddings = model.encode(topics)

# Convert to numpy
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save data
faiss.write_index(index, "topics.index")

with open("topics.txt", "w") as f:
    for t in topics:
        f.write(t + "\n")

print("✅ FAISS vector DB created successfully")
