from collections import deque

def water_jug_bfs(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)])   
    
    print("Steps to reach the goal:")
    while queue:
        x, y = queue.popleft()
        
        
        if x == target or y == target:
            print(f"Reached target state: ({x}, {y})")
            return True
        
        
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        print(f"Current state: ({x}, {y})")
        
        
        next_states = [
            (jug1, y),  
            (x, jug2),  
            (0, y),     
            (x, 0),     
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),  
            (x + min(y, jug1 - x), y - min(y, jug1 - x))   
        ]
        
        for state in next_states:
            if state not in visited:
                queue.append(state)
    
    return False


water_jug_bfs(4, 3, 2)
