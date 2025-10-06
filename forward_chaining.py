# Knowledge base: rules and facts
rules = {
    "A and B -> C": (["A", "B"], "C"),
    "C and D -> E": (["C", "D"], "E"),
    "E -> Goal":    (["E"], "Goal")
}

facts = {"A", "B", "D"}  # initial facts

def forward_chaining(rules, facts, goal):
    added = True
    while added:
        added = False
        for name, (conds, result) in rules.items():
            if all(c in facts for c in conds) and result not in facts:
                facts.add(result)
                print(f"Rule applied: {name}, New fact: {result}")
                if result == goal:
                    return True
                added = True
    return False

# Run forward chaining
goal = "Goal"
if forward_chaining(rules, facts, goal):
    print(f"✅ Goal '{goal}' derived!")
else:
    print(f"❌ Goal '{goal}' not reached.")
