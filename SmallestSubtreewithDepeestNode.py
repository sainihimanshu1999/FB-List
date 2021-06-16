'''
length of the subtree should be least but it should be deep
'''

def deepest(root):
    def dfs(node,depth):

        if not node:
            return node,depth

        left,leftD = dfs(node.left,depth+1)
        right,rightD = dfs(node.right,depth+1)

        if leftD>rightD:
            return left,leftD

        elif rightD>leftD:
            return right,rightD
        
        else:
            return node,leftD

    return dfs(root,0)[0]