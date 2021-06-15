'''
We are using API of isBadVersion, which tell us whether this number is bad or not and then we use bindary search in this
'''

def firsBadVersion(n):
    low = 1
    high = n
    while low<high:
        if isBadVersion(n):
            low = mid

        else:
            high = mid+1
    return low
