'''
basic usauge of stack in this question
'''

def InvalidParanthesis(s):
    s = list(s)
    stack = []

    for i,char in enumerate(s):
        if char == '(':
            stack.append(i)

        if char ==')':
            if stack:
                stack.pop()
            else:
                s[i] = ''
    while stack:
        s[stack.pop()] = ''
    
    return ''.join(s)


s = "lee(t(c)o)de)"
print(InvalidParanthesis(s))
        