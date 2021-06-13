'''
We use totpological sort here. Topological sort is usually used for detecting cycles in directed edge graph.
'''

from collections import defaultdict

def courseScedule(nums,courses):
    global graph
    graph = defaultdict(set)

    for i,j in courses:
        graph[i].add(j)

    global visited
    global cycle

    visited = [0]*nums
    cycle = 0

    for i in range(nums):
        if cycle == 1:
            break
        if visited[i]==0:
            dfs(i)
    
    return cycle == 0

def dfs(start):
    if cycle == 1:
        return
    
    if visited[start]==1:
        cycle == 1

    if visited[start]==0:
        visited[start] =1
        for ni in graph[start]:
            dfs(ni)
        visited[start] = 2



