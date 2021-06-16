'''
To check if a given string is a palindrome after deleting at most one, we have to check inside of the 
'''

def validPalindrome(s):
    low = 0
    high = len(s)-1

    while low<high:
        if s[low]!=s[high]:
            one = s[low:high]
            two = s[low+1:high+1]
            return one == one[::-1] or two == two[::-1]
        low+=1
        high-=1
    return True


s = "abdxa"
print(validPalindrome(s))