'''
Binary search can only work in sorted part of the arrays, hence in rotated arrays we need to find the array part which
is sorted and find our element in it
'''

def rotated(nums,target):
    if not nums: return -1

    low,high =0,len(nums)-1

    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            return mid
        
        if nums[low]<=nums[mid]:
            if nums[low]<=target<=nums[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if nums[mid]<=target<=nums[high]:
                low = mid+1
            else:
                high = mid -1

    return -1


nums = [4,5,6,7,0,1,2]
target = 0

print(rotated(nums,target))