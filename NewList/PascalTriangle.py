
#dp formula
def pascal(n):
    dp = [[0]*n for _ in range(n)]

    for j in range(n):
        dp[j][0] = 1

    for i in range(1,n):
        for j in range(1,i+1):
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j]

    return dp[n-1]


#recusive Formula

def pascal2(n):
    if n == 0:
        return []

    if n==1:
        return [[1]]

    result = []

    for i in pascal2(n-1):
        result.append(i)

    temp_row = result[-1]
    new_row = [1]

    for i in range(len(temp_row)-1):
        new_row.append(temp_row[i]+temp_row[i+1])
    new_row.append(1)

    result.append(new_row)

    return result


print(pascal2(4))