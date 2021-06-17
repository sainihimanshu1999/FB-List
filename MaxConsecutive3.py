'''
max length of consecutive ones ans with k most zeroes
'''

def maxConsecutiveOnes(nums,k):
    left=right=0

    for right in range(len(nums)):
        
        if nums[right] == 0:
            k-=1

        if k<0:
            if nums[left]==0:
                k+=1
            
            left+=1
    return right-left+1


nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(maxConsecutiveOnes(nums,k))