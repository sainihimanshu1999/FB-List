'''
we heare use the inbuilt function called divmod which returns us quotient and remainder
'''

def fractionDecimal(numerator,denominator):
    quo,rem = divmod(abs(numerator),abs(denominator))
    sign = '-' if numerator*denominator<0 else ''
    remainders = {}
    result = [str(quo),'.']

    while rem>0 and rem not in remainders:
        remainders[rem] = len(result)
        quo,rem = divmod(abs(rem)*10,abs(denominator))
        result.append(str(quo))

    if rem in remainders:
        index = remainders[rem]
        result.insert(index,'(')
        result.append(')')

    return ''.join(result).rstrip('.')

print(fractionDecimal(2,3))