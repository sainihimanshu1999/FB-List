'''
Calculatin power of numbers without using built in functions
'''

def pow(x,n):
    if n==0:
        return 1
    if n<0:
        return pow(1/x,-n)

    num = pow(x,n//2)

    if n%2==0:
        return num*num

    if n%2==1:
        return num*num*x


print(pow(2,-3))
