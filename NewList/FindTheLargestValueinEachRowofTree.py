'''
we can do this question by both bfs and dfs, but i'll only gonna do dfs
'''

def largestValue(root):
    result = []

    def dfs(node,level):
        if not node: return []

        if len(result) == level:
            result.append(node.val)

        else:
            result[level] = max(result[level],node.val)

        dfs(node.left,level+1)
        dfs(node.righ,right+1)

    dfs(root,0)
    return result