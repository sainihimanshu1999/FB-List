def merge(nums1,nums2):
    arr = []
    i=0
    j=0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            arr.append(nums1[i])
            i += 1
        else:
            arr.append(nums2[j])
            j+=1
            

    while i<len(nums1):
        arr.append(nums1[i])
        i+=1

    while j<len(nums2):
        arr.append(nums2[j])
        j +=1
        
    return arr




def inplace(nums1,nums2): 
    m = len(nums1)
    n = len(nums2)

    nums1 = nums1+[0]*n

    while m and n:
        if nums1[m-1]>=nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -=1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -=1

    if n>0:
        nums1[:n] = nums2[:n]

    return nums1



nums1 = [1,2,3]
nums2 = [2,5,6]



print(inplace(nums1,nums2))