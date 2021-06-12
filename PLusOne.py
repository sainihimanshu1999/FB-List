'''
This one is quite easy question which has an intutive solution
'''

def plusone(nums):
    if len(nums)==0:
        nums = [1]
    elif nums[-1]==9:
        nums = plusone(nums[:-1])
        nums.extend([0])
    else:
        nums[-1] +=1
    return nums

print(plusone([1,2,9]))