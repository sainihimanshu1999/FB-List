'''
We have to find the maximum sum of contigous subarray in the given array
'''

def maxSum(nums):
    for i in range(1,len(nums)):
        if nums[i-1]>0:
            nums[i] += nums[i-1]

    return max(nums)


print(maxSum([-2,1,-3,4,-1,2,1,-5,4]))