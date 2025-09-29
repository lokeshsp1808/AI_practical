from itertools import permutations

# Distance matrix (symmetric)
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(dist)
cities = list(range(n))
min_cost = float('inf')
best_path = []

# Generate all possible permutations of cities (except starting city 0)
for perm in permutations(cities[1:]):
    path = [0] + list(perm) + [0]  # start and end at city 0
    cost = sum(dist[path[i]][path[i+1]] for i in range(n))
    if cost < min_cost:
        min_cost = cost
        best_path = path

print("Optimal path:", best_path)
print("Minimum cost:", min_cost)