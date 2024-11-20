def backward_chaining(knowledge_base, query):
    for rule in knowledge_base:
        antecedent, consequent = rule
        if consequent == query:
            if all(backward_chaining(knowledge_base, a) for a in antecedent):
                return True
    return False

# Example Knowledge Base
knowledge_base = [
    (("A", "B"), "C"),
    ("A", "B"),
    ("B", "C")
]

# Query
query = "C"

if backward_chaining(knowledge_base, query):
    print("Query is true")
else:
    print("Query is false")
