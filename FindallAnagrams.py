'''
using two counter to count the number of elements
'''
from collections import Counter

def findAnagrams(s,p):
    countP = Counter(p)
    countS = Counter(s[:len(p)])

    i=0
    j=len(p)

    result = []

    while j<=len(s):
        if countP == countS:
            result.append(i)

        countS[s[i]] -= 1
        if countS[s[i]]<=0:
            countS.pop(s[i])

        if j<len(s):
            countS[s[j]] += 1

        j+=1
        i+=1

    return result


s = "cbaebabacd"
p = "abc"

print(findAnagrams(s,p))

