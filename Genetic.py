import random

# Distance matrix for 5 cities
dist = [
    [0, 2, 9, 10, 7],
    [2, 0, 6, 4, 3],
    [9, 6, 0, 8, 5],
    [10, 4, 8, 0, 6],
    [7, 3, 5, 6, 0]
]

num_cities = len(dist)
pop_size = 10
generations = 50
mutation_rate = 0.1

# Create a random route
def create_route():
    route = list(range(num_cities))
    random.shuffle(route)
    return route

# Calculate total distance of a route
def total_distance(route):
    return sum(dist[route[i]][route[i+1]] for i in range(num_cities-1)) + dist[route[-1]][route[0]]

# Selection based on fitness (shorter distance = higher chance)
def selection(pop):
    fitness = [1/total_distance(r) for r in pop]
    total = sum(fitness)
    probs = [f/total for f in fitness]
    return random.choices(pop, probs, k=2)

# Crossover two parents
def crossover(p1, p2):
    start, end = sorted(random.sample(range(num_cities), 2))
    child = p1[start:end] + [city for city in p2 if city not in p1[start:end]]
    return child

# Mutate a route
def mutate(route):
    if random.random() < mutation_rate:
        i, j = random.sample(range(num_cities), 2)
        route[i], route[j] = route[j], route[i]
    return route

# Initialize population
population = [create_route() for _ in range(pop_size)]
best = min(population, key=total_distance)
best_dist = total_distance(best)

# Run GA
for _ in range(generations):
    new_pop = []
    for _ in range(pop_size):
        p1, p2 = selection(population)
        child = mutate(crossover(p1, p2))
        new_pop.append(child)
    population = new_pop
    curr_best = min(population, key=total_distance)
    if total_distance(curr_best) < best_dist:
        best = curr_best
        best_dist = total_distance(curr_best)

print("Best Route:", best)
print("Best Distance:", best_dist)