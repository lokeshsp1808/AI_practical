from heapq import heappush, heappop

def a_star(grid, start, goal):
    h = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])      # Manhattan heuristic
    rows, cols = len(grid), len(grid[0])
    open_set = [(h(start, goal), 0, start)]                   # (f, g, node)
    came_from, g_score, visited = {}, {start: 0}, set()

    while open_set:
        f, g, node = heappop(open_set)
        if node == goal:                                      # Goal reached → reconstruct path
            path = [node]
            while node in came_from:
                node = came_from[node]
                path.append(node)
            return path[::-1]

        if node in visited: continue
        visited.add(node)

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:            # 4-direction moves
            nx, ny = node[0] + dx, node[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_g = g + 1
                if (nx, ny) not in g_score or new_g < g_score[(nx, ny)]:
                    g_score[(nx, ny)] = new_g
                    heappush(open_set, (new_g + h((nx, ny), goal), new_g, (nx, ny)))
                    came_from[(nx, ny)] = node
    return None


# Example grid (0 = free cell, 1 = obstacle)
grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start, goal = (0, 0), (4, 4)

print("Shortest Path Found by A*:", a_star(grid, start, goal))
