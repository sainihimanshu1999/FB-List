
def maxpathsum(root):
    self.maxpath = 0
    def dfs(node):
        if not node: return 0

        right = max(dfs(node.right),0)
        left = max(dfs(node.left),0)

        pathsum = node.val + left+right
        self.maxpath = max(self.maxpath,pathsum)

        return node.val + max(left,right)

    dfs(root)
    return self.maxpath