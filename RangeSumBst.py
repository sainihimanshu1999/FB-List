'''
Sort of an easy question, but can be done easily, just try to use recurrsion more efficiently
'''

def rangeSum(root,low,high):
    if not root: return 0
    sumi = 0

    if root.val>low:
        sumi+= rangeSum(root.left,low,high)
    
    if root.val<high:
        sumi+= range(root.right,low,high)

    if low<=root.val<=high:
        sumi+= root.val

    return sumi