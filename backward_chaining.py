# Knowledge base: rules and facts
rules = {
    "A and B -> C": (["A", "B"], "C"),
    "C and D -> E": (["C", "D"], "E"),
    "E -> Goal":    (["E"], "Goal")
}

facts = {"A", "B", "D"}  # known facts

def backward_chaining(rules, facts, goal, depth=0):
    indent = "  " * depth
    print(f"{indent}Proving {goal}...")
    
    if goal in facts:
        print(f"{indent}✔ {goal} is a known fact.")
        return True
    
    for name, (conds, result) in rules.items():
        if result == goal:
            print(f"{indent}Using rule: {name}")
            if all(backward_chaining(rules, facts, c, depth+1) for c in conds):
                print(f"{indent}✔ {goal} proven by {name}")
                return True
    
    print(f"{indent}✘ Failed to prove {goal}")
    return False

# Run backward chaining
goal = "Goal"
if backward_chaining(rules, facts, goal):
    print(f"✅ Goal '{goal}' derived!")
else:
    print(f"❌ Goal '{goal}' not reached.")
