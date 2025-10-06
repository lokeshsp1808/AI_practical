import math

# Alpha-Beta Pruning
def alphabeta(depth, node, alpha, beta, maximizing, values, max_depth):
    if depth == max_depth:
        return values[node]
    
    if maximizing:
        value = -math.inf
        for i in range(2):  # binary tree
            value = max(value, alphabeta(depth+1, node*2+i, alpha, beta, False, values, max_depth))
            alpha = max(alpha, value)
            if alpha >= beta: break   # prune
        return value
    else:
        value = math.inf
        for i in range(2):
            value = min(value, alphabeta(depth+1, node*2+i, alpha, beta, True, values, max_depth))
            beta = min(beta, value)
            if alpha >= beta: break   # prune
        return value

# Example leaf values
values = [3, 5, 6, 9, 1, 2, 0, -1]  # 8 leaves

print("Leaf nodes:", values)
res = alphabeta(0, 0, -math.inf, math.inf, True, values, 3)
print("Optimal value:", res)

