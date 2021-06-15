def addStrings(s1,s2):
    result = []
    carry = 0
    m = len(s1)-1
    n = len(s2)-1

    while m>=0 or n>=0:
        x1 = ord(s1[m])-ord('0') if m>=0 else 0
        x2 = ord(s2[n])-ord('0') if n>=0 else 0

        value = (x1+x2+carry)%10
        carry = (x1+x2+carry)//10

        result.append(value)
        m-=1
        n-=1

    if carry:
        result.append(carry)

    return ''.join(str(x) for x in result[::-1])


print(addStrings('19','38'))