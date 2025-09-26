time = 0  

def dfs(graph, node, visited, entry, exit_time):
    global time
    visited.add(node)
    time += 1
    entry[node] = time   
    print(f"Visited {node} at entry time {entry[node]}")

   
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, entry, exit_time)

    
    time += 1
    exit_time[node] = time
    print(f"Backtracked {node} at exit time {exit_time[node]}")


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


visited = set()
entry, exit_time = {}, {}
dfs(graph, 'A', visited, entry, exit_time)

print("\nFinal Entry Times:", entry)
print("Final Exit Times:", exit_time)
