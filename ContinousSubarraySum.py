'''
We use basic dictionary in this question, and if sum(i,j)%k == 0 it means sum(0,j)-sum(0,i-1) hence if two
sums have same remainder we know sum(i,j) can be divided by k
'''

def subarraySum(nums,k):
    dic = {0:-1}
    sumi = 0

    for i in range(len(nums)):
        sumi += nums[i]

        if k!=0:
            sumi = sumi%k
        
        if sumi in dic:
            if (i-dic[sumi]>1):
                return True
        else:
            dic[sumi] = i
    return False


s = [24,2,4,6,7]

print(subarraySum(s,6))