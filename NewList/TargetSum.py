'''
This problem is like 0/1 knapsack problem and we really have to use dfs to source all the possibilties of our answer
'''

def targetSum(target,nums):
    index = len(nums)-1
    curr_sum = 0
    memo= {}

    def dfs(index,curr_sum,memo):
        if (index,curr_sum) in memo:
            return memo[(index,curr_sum)]

        if index<0 and curr_sum == target:
            return 1

        if index<0:
            return 0


        positive = dfs(index-1,curr_sum+nums[index],memo)
        negative = dfs(index-1,curr_sum-nums[index],memo)

        memo[(index,curr_sum)] = positive+negative
        return memo[(index,curr_sum)]
    return dfs(index,curr_sum,memo)


nums = [1,1,1,1,1]
t = 3

print(targetSum(t,nums))