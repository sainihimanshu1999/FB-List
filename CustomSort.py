'''
The string1 should have a same order as string2
'''
from collections import Counter

def customSort(order,chars):
    result = []
    count = Counter(chars)

    for c in order:
        if count[c]:
            result.extend(c*count.pop(c))

    for c,v in count.items():
        result.extend(c*v)

    return ''.join(result)

order = 'cab'
chars = 'abcd'

print(customSort(order,chars))

