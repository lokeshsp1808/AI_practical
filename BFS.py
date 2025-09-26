from collections import deque

def bfs(graph, start):
    visited = set()                 
    queue = deque([(start, 0)])    
    visited.add(start)

    print("BFS Traversal with Levels:")
    while queue:                    
        node, level = queue.popleft()  
        print(f"Node: {node}, Level: {level}")

        for neighbor in graph[node]:  
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))  
    

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


bfs(graph, 'A')
