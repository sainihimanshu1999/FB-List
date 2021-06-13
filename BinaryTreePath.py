
def binaryPath(root):
    result  = []
    def dfs(node,path):
        #if not node: return
        if not node.left and not node.right:
            path.append(str(node.val))
            result.append(path)
            return result
        
        if node.left:
            dfs(node.left,path+str(node.va)+'->')
        
        if node.right:
            dfs(node.right,path+str(node.val)+'->')

    dfs(root,'')

    return result

        
