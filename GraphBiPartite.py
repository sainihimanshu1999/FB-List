'''
In this question we use BFS + coloring algortihm to find the answer
'''

def bipartite(graph):
    seen = {}

    for i in range(len(graph)):
        if i not in seen:
            if not check(graph,i,seen):
                return False
    return True

def check(graph,start,seen):
    q = [(start,1)]

    while len(q)>0:
        node,color = q.pop(0)

        if node in seen:
            if seen[node]!=color:
                return False
            continue
        seen[node]=color

        vertices = graph[node]
        for v in vertices:
            q.append((v,-color))
    return True

graph = [[1,3],[0,2],[1,3],[0,2]]
print(bipartite(graph))
