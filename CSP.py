colors = ["Red", "Green", "Blue"]

neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':  ['NT', 'SA', 'NSW'],
    'NSW':['Q', 'SA', 'V'],
    'V':  ['SA', 'NSW'],
    'T':  []
}

def is_valid(assignment, state, color):
    return all(assignment.get(neigh) != color for neigh in neighbors[state])

def backtrack(assignment):
    if len(assignment) == len(neighbors):
        return assignment
    state = next(s for s in neighbors if s not in assignment)  # pick unassigned
    for color in colors:
        if is_valid(assignment, state, color):
            assignment[state] = color
            result = backtrack(assignment)
            if result: return result
            del assignment[state]
    return None

solution = backtrack({})
print("Solution:", solution)
