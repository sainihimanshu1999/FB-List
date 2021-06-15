'''
Using dictionary in this question
'''

def subarraySum(nums,k):
    dic = {0:1}
    sumi = 0
    count = 0

    for num in nums:
        sumi += num

        if sumi-k in dic:
            count += dic[sumi-k]

        if sumi in dic:
            dic[sumi] += 1
        
        else: 
            dic[sumi] = 1
    
    return count
    
