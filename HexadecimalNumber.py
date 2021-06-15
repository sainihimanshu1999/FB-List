'''
Converting numbers into there hexadecimal form
'''

def hexa(num):
    if num == 0: return '0'

    mp = '0123456789abcdef'
    ans = ''

    for i in range(8):
        n = num&15
        char = mp[n]
        ans = char+ans
        num = num>>4
    return ans.lstrip('0')

print(hexa(890))
