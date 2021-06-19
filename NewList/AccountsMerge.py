'''
This is a graph question in which we had use dfs
'''

from collections import defaultdict

def accountMerge(accounts):
    graph = defaultdict(list)
    for i,account in enumerate(accounts):
        for j in range(1,len(account)):
            email = account[j]
            graph[email].append(i)

    result = []
    visited = [False]*(len(accounts))
    def dfs(i,emails):
        if visited[i]: return
        visited[i] = True

        for j in range(1,len(accounts[i])):
            email = accounts[i][j]
            emails.add(email)
            for ni in graph[email]:
                dfs(ni,emails)

    for i,account in enumerate(accounts):
        if visited[i]:
            continue
        name,emails = account[0],set()
        dfs(i,emails)
        result.append([name]+sorted(emails))
    return result

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
print(accountMerge(accounts))