'''
In this question we have to find longest increasing path in a matrix. we will use basic dfs in this question
'''

def path(matrix):
    m,n=len(matrix),len(matrix[0])
    dp = [[0]*n for _ in range(m)]
    result = []
    def dfs(i,j):
        if not dp[i][j]:
            val = matrix[i][j]

            if i and val>matrix[i-1][j]:
                up = dfs(i-1,j)
            else:
                up = 0

            if i<m-1 and val>matrix[i+1][j]:
                down = dfs(i+1,j)
            else:
                down = 0

            if j and val>matrix[i][j-1]:
                left = dfs(i,j-1)
            else:
                left = 0

            if j<n-1 and val>matrix[i][j+1]:
                right = dfs(i,j+1)
            else:
                right = 0

            dp[i][j] = 1+max(up,down,right,left)

        return dp[i][j]

    for i in range(m):
        for j in range(n):
            result.append(dfs(i,j))

    return max(result)


matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(path(matrix))


