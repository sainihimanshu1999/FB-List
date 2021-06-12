'''
we use simple two pointer approach in this question
'''
from collections import Counter

def window(s,t):
    target_counter = Counter(t)
    target_len = len(t)
    start,end =0,0
    minWindow = ''

    for end in range(len(s)):
        if target_counter[s[end]]>0:
            target_len -=1
        target_counter[s[end]] -=1

        while not target_len:
            window_len = end-start+1
            if not minWindow or len(minWindow)>window_len:
                minWindow = s[start:end+1]

            target_counter[s[start]] += 1

            if target_counter[s[start]]>0:
                target_len +=1
            
            start +=1

    return minWindow



s = "ADOBECODEBANC"
t = "ABC"

print(window(s,t))
            