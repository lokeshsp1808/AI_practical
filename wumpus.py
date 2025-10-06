# Very simplified Wumpus inference demo
KB = {}  # Knowledge base of percepts

# Add percept to KB
def tell(cell, percept):
    KB[cell] = percept

# Ask if a cell is safe based on KB
def ask_safe(cell):
    # If no breeze or stench in neighbors, assume safe
    for (pos, percept) in KB.items():
        if 'Breeze' in percept and cell in neighbors(pos): return False
        if 'Stench' in percept and cell in neighbors(pos): return False
    return True

def neighbors(pos):
    x,y = pos
    return [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

# Example usage:
tell((1,1), ['Breeze'])   # agent perceives breeze at (1,1)
print("Is (2,1) safe?", ask_safe((2,1)))
print("Is (1,2) safe?", ask_safe((1,2)))
