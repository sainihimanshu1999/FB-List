'''
Kth smallest element, we can use inorder traversal for making it basic
'''

def kthElement(root,k):
    x = []
    def ino(root):
        root.left
        x.append(root.val)
        root.right
    return x[k-1]
        