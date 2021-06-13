
def LCA(root,p,q):
    if root == p and root == q:
        return root

    if root.left:
        left = LCA(root.left,p,q)
    
    if root.right:
        right = LCA(root.right,p,q)

    if left and right:
        return root
        
    else:
        return left or right

