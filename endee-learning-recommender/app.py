from search import search_topics

print("🤖 AI Learning Path Recommender (Endee Powered)")

user_input = input("Enter your learning goal: ")

results = search_topics(user_input)

print("\n📚 Recommended Learning Path:\n")

for r in results:
    print("-", r)
