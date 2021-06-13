'''
we maintain left and right array to see before and after element product and then product them into our answer
'''

def product(nums):
    left = [1]*(len(nums))
    right =[1]*(len(nums))
    answer = [1]*len(nums)


    for i in range(1,len(nums)):
        left[i] =left[i-1]*nums[i-1]


    for i in range(len(nums)-2,-1,-1):
        right[i] = right[i+1]*nums[i+1]


    for i in range(len(nums)):
        answer[i] = left[i]*right[i]

    return answer

nums = [1,2,3,4]
print(product(nums))

