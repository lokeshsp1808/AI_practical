import math

def win(b):
    for a,b1,c in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]:
        if board[a] != ' ' and board[a] == board[b1] == board[c]: return board[a]
    return None

def minimax(b, turn):
    w = win(b)
    if w: return {'X':10,'O':-10}[w]
    if ' ' not in b: return 0
    best = -math.inf if turn=='X' else math.inf
    for i in range(9):
        if b[i]==' ':
            b[i]=turn
            val=minimax(b,'O' if turn=='X' else 'X')
            b[i]=' '
            best = max(best,val) if turn=='X' else min(best,val)
    return best

def best_move(b):
    return max((minimax([*b[:i],'X',*b[i+1:]],'O'), i) for i in range(9) if b[i]==' ')[1]

board = ['X','O','X',' ','O',' ',' ',' ',' ']
print("Best move for X:", best_move(board))
