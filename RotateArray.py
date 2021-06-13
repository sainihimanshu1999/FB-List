'''
We have to rotatet this array to the right by k steps, we have to do this in constant space
'''

def roatate(nums,k):
    n = len(nums)
    k = k%n

    start = 0
    count = 0


    while count<n:
        current,prev = start,nums[start]
        while True:
            next_index = (current+k)%n
            nums[next_index],prev = prev,nums[next_index]
            current = next_index
            count +=1

            if start==current:
                break
        start+=1
    return nums


nums = [1,2,3,4,5,6,7]
print(roatate(nums,3))
