import math

wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
def winner(b): return next((b[a] for a,b1,c in wins if b[a]!=' ' and b[a]==b[b1]==b[c]),None)
def term(b):
    w=winner(b)
    return (True,1 if w=='X' else -1) if w else (True,0) if ' ' not in b else (False,None)

def minimax(b, maxp):
    end,score=term(b)
    if end: return score
    scores=[(b.__setitem__(i,'X' if maxp else 'O'),minimax(b,not maxp),b.__setitem__(i,' ')) or v
            for i in range(9) if b[i]==' ' for v in [0]]
    return (max if maxp else min)(scores)

def best_move(b, p='X'):
    best,move=(-math.inf,-1) if p=='X' else (math.inf,-1)
    for i in range(9):
        if b[i]==' ':
            b[i]=p; val=minimax(b,p=='O'); b[i]=' '
            if (p=='X' and val>best) or (p=='O' and val<best): best,move=val,i
    return move,best

# 🔹 Different board setup
board=['X','O',' ',' ','X',' ',' ','O',' ']

mv,val=best_move(board,'X')
for r in range(3): print(board[3*r:3*r+3])
print(f"\nBest move for X: {mv}, Score={val}")
