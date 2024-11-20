# Initial facts
facts = {"A", "B"}

# Inference rules: 
# (Condition, Conclusion)
rules = [
    ({"A", "B"}, "C"),  # If we know A and B, we can conclude C
    ({"C"}, "D")        # If we know C, we can conclude D
]

# Forward chaining loop
new_fact_added = True
while new_fact_added:
    new_fact_added = False
    for condition, conclusion in rules:
        # If the condition is in facts and conclusion is not already in facts
        if condition.issubset(facts) and conclusion not in facts:
            facts.add(conclusion)
            new_fact_added = True
            print(f"New fact inferred: {conclusion}")

print("Final facts:", facts)
