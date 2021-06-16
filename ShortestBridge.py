'''
Shortest Brridge between islands, can be found by first using dfs cover all those ones which comes under the single
island and then use bfs two find the shortest path between two islands
'''

def bridges(grid):
    stack = []
    m,n = len(grid),len(grid[0])

    def dfs(grid,row,col,m,n,stack):
        if row<0 or row>=m or col<0 or col>=n or grid[row][col]!=1:
            return 
        grid[row][col] = 2
        stack.append((row,col))
        dfs(grid,row-1,col,m,n,stack)
        dfs(grid,row+1,col,m,n,stack)
        dfs(grid,row,col-1,m,n,stack)
        dfs(grid,row,col+1,m,n,stack)

    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                dfs(grid,i,j,m,n,stack)
                found = True
                break
        if found:
            break

    steps = 0
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while stack:
        level = []
        size = len(stack)
        while size>0:
            temp = stack.pop()
            size -=1
            x,y = temp[0],temp[1]

            for dx,dy in dirs:
                tx=dx+x
                ty=dy+y

                if tx<0 or tx>=m or ty<0 or ty>=n or grid[tx][ty]==2:
                    continue
                if grid[tx][ty]==1:
                    return steps 
                grid[tx][ty] = 2
                level.append((tx,ty))
        steps+=1
        stack=level
    return -1


grid = [[0,1,0],[0,0,0],[0,0,1]]
print(bridges(grid))
            