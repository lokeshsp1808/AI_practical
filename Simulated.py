import math, random

def simulated_annealing(f, x0, T=1.0, T_min=1e-5, alpha=0.99):
    x, fx = x0, f(x0)
    while T > T_min:
        # small random neighbor
        x_new = x + random.uniform(-0.5, 0.5)
        fx_new = f(x_new)
        # accept if better, or with a probability if worse
        if fx_new > fx or random.random() < math.exp((fx_new - fx) / T):
            x, fx = x_new, fx_new
        T *= alpha    # cool down
    return x, fx

f = lambda x: -(x - 3)**2 + 9
best_x, best_fx = simulated_annealing(f, random.uniform(0, 6))
print(f"Best solution: x = {best_x:.3f}, f(x) = {best_fx:.3f}")
