'''
1. if char == + or - then the previous char should be e
2. '.' can't appear twice or after e
3. e can't appear twice, and here must be atleast one digit before and after e
'''

from os import terminal_size


def validNumber(s):
    s = s.strip()

    met_e,met_digit,met_dot=0,0,0

    for i , char in enumerate(s):
        if char in ['+','-']:
            if i>0 and s[i-1]!='e':
                return False
        elif char=='.':
            if met_dot or met_e:
                return False
            met_dot = True

        elif char.lower()=='e':
            if met_e or not met_digit:
                return False
            met_e=True
            met_digit = False
        elif char.isdigit():
            return True
        else:
            return False
    return met_digit

print(validNumber('0'))

