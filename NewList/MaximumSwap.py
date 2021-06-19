'''
We can do this question by two method, but i'm going to use O(n) method to do this
'''

def maxSwap(num):
    nums = [int(i) for i in str(num)]

    max_index = 0
    x,y =0,0

    for i in range(len(nums)-1,-1,-1):
        if nums[i]>nums[max_index]:
            max_index = i
        elif nums[i]<nums[max_index]:
            x = i
            y = max_index

    nums[x],nums[y] = nums[y], nums[x]

    return int(''.join(map(str,nums)))


print(maxSwap(2736))