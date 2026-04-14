#ai-learning-path-generator

📌 Overview
This project is an AI-based study topic recommendation system that suggests relevant topics based on user input. It demonstrates the concept of Retrieval Augmented Generation (RAG) using vector similarity.

🎯 Objective
To help students identify what topics to study next by analyzing similarity between concepts and recommending related topics.

🧠 How It Works
User Input → Convert to Embedding → Store/Search using Endee → Retrieve Similar Topics → Generate Recommendations

⚙️ Tech Stack
Python
Endee (Vector Database)
RAG (Retrieval Augmented Generation)
🔍 Use of Endee
This project uses Endee as a vector database to:

Store topic embeddings
Perform semantic similarity search
Retrieve relevant topics efficiently
🚀 Features
Topic recommendation system
Semantic similarity search
AI-based suggestion logic
📂 Project Structure
student-ai-search/ │── app.py │── data.txt │── requirements.txt │── README.md

▶️ Setup Instructions
Clone the repository
Navigate to the project folder
Install dependencies
Run the application
📈 Future Improvements
Add chatbot interface
Add real-time user interaction
Integrate full Endee API for real vector search
📚 Conclusion
This project demonstrates how AI and vector databases can be used to build intelligent recommendation systems for real-world applications.

📝 Note
This is a simplified implementation to demonstrate the concept of RAG and vector search using Endee.
