import random

def hill_climbing(f, x_start, step=0.1, max_iter=1000):
    x = x_start
    for _ in range(max_iter):
        # Two neighbors: left and right step
        neighbors = [x - step, x + step]
        # Pick the best neighbor
        best = max(neighbors, key=f)
        if f(best) <= f(x):   # No better neighbor → stop
            break
        x = best
    return x, f(x)

# Function to maximize
f = lambda x: -(x - 3)**2 + 9

# Random start between 0 and 6
solution, value = hill_climbing(f, random.uniform(0, 6))
print(f"Best solution: x = {solution:.2f}, f(x) = {value:.2f}")
