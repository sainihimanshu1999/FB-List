'''
using memoization technique
'''

def partialsum(nums):
    def dfs(nums,target,memo):
        if target<0:
            return False

        if target==0:
            return True

        if target in memo:
            return False

        memo.add(target)

        for i,n in enumerate(nums):
            if dfs(nums[i+1:],target-n,memo):
                return True

        return False
    
    if sum(nums)%2 !=0:
        return False
    return dfs(nums,sum//2,set())


    