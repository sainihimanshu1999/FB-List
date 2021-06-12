'''
It is similar to previous question but the only difference is this array conatins duplicate elements
'''

def rotated(nums,target):
    if not nums: return False
    low,high = 0,len(nums)-1

    while low<=high:
        mid = (low+high)//2
        if nums[mid] == target:
            return True
        
        if nums[low]<nums[mid]:
            if nums[low]==nums[mid]:
                low+=1
                continue
            if nums[low]<=nums[target]<=nums[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if nums[mid]<=target<=nums[high]:
                low = mid+1
            else:
                high = mid-1
    return False