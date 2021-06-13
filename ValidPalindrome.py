'''
This question can be solved usign two methods
'''


#extraSpace less time

def validpalin(s):
    a = ''.join(i for i in s if i.isalnum()).lower()
    return a == a[::-1]




#not extra space more time


def validpalin2(s):
    low,high =0,len(s)-1

    while low<high:
        while low<high and not s[low].isalnum():
            low+=1
        while low<high and not s[high].isalnum():
            high -=1
        if s[low].lower() != s[high].lower():
            return False
        low+=1
        high -=1
    return True        

s = "A man, a plan, a canal: Panama"
print(validpalin2(s))