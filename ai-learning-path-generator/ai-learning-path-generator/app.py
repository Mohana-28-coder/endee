# AI Learning Path Generator

# Load topics from file
def load_data():
    with open("data.txt", "r") as file:
        topics = file.read().splitlines()
    return topics

# Recommendation logic
def generate_path(user_input, topics):
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
learning_path = generate_path(user_input, topics)

print("\nSuggested Learning Path:")
for r in learning_path:
    print("-", r)
