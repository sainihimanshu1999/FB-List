'''
We solve this question using two different approaches, one is using bit manipulation an other is using recursive approach
'''


#recursive

def pow(x,n):
    if abs(x)<1e-40:return 0
    if n==0: return 1
    if n<0: return pow(1/x,-n)

    lower = pow(x,n//2)
    if n%2==0: return lower*lower
    if n%2==1: return lower*lower*x


# bit manipulation


def pow2(x,n):
    m = abs(n)
    ans =1.0

    while m:
        if m&1:
            ans = ans*x
        x = x*x
        m>>=1
    return ans if n>=0 else 1/ans


print(pow2(2,-3))