# AI Study Topic Recommender

# Load topics from file
def load_data():
    with open("data.txt", "r") as file:
        topics = file.read().splitlines()
    return topics

# Recommendation logic
def recommend_topic(user_input, topics):
    results = []
    
    for topic in topics:
        if user_input.lower() in topic.lower():
            results.append(topic)
    
    if not results:
        return ["algebra", "calculus", "probability"]
    
    return results

# Main program
topics = load_data()

user_input = input("Enter a topic: ")
recommendations = recommend_topic(user_input, topics)

print("\nRecommended Topics:")
for r in recommendations:
    print("-", r)
