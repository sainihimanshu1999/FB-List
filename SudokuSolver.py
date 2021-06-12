'''
In this question we backtrack very easily, it's quite difficult to understand but pretty worth it
'''
from collections import defaultdict
from collections import deque

def sudoku(grid):
    rows,cols = defaultdict(set),defaultdict(set)
    triples,seen = defaultdict(set),deque([])

    for r in range(9):
        for c in range(9):
            if grid[r][c]!='.':
                rows[r].add(grid[r][c])
                cols[c].add(grid[r][c])
                triples[(r//3,c//3)].add(grid[r][c])
            else:
                seen.append((r,c))

    def dfs():
        if not seen:
            return True
        r,c =seen[0]
        t = (r//3,c//3)

        for dig in {'1','2','3','4','5','6','7','8','9'}:
            if dig not in rows[r] and dig not in cols[c] and dig not in triples[t]:
                grid[r][c]=dig
                rows[r].add(dig)
                cols[c].add(dig)
                triples[t].add(dig)
                seen.popleft()
                if dfs():
                    return True
                else:
                    grid[r][c] = '.'
                    rows[r].discard(dig)
                    cols[c].discard(dig)
                    triples[t].discard(dig)
                    seen.appendleft((r,c))
        return False

    dfs() 
    return board



board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(sudoku(board))




