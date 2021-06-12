'''
Adding Two Binary numbers, we we add usually we use a varaibel called carry
'''

def binary(a,b):
    carry = 0
    answer = ''

    a = list(a)
    b = list(b)

    while a or b or carry:
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())


        answer += str(carry%2)
        carry = carry//2

    return answer[::-1]


print(binary('11','1'))

