'''
While calculating the combinations sum, we chalk out the path using dfs traversal
'''

def combinationSum(nums,target):
    if not nums: return []

    result = []
    dfs(nums,target,[],result)
    return result

def dfs(nums,target,path,result):
    if target<0:
        return 

    if target == 0:
        result.append(path)
        return result

    for i in range(len(nums)):
        dfs(nums[i:],target-nums[i],path+[nums[i]],result)



candidates = [2,3,6,7]
target = 7

print(combinationSum(candidates,target))