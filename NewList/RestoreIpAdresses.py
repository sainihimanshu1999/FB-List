'''
we have to restore idp adress, quite tricky and clever backtracking
'''

def ipAdrress(s):
    result = []
    dfs(s,0,'',result)
    return result

def dfs(s,idx,path,result):
    if idx > 4:
        return 
    if idx == 4 and not s:
        result.append(path[:-1])
        return result
    for i in range(1, len(s)+1):
        if s[:i]=='0' or (s[0]!='0' and 0 < int(s[:i]) < 256):
            dfs(s[i:], idx+1, path+s[:i]+".", result)


s = "25525511135"
print(ipAdrress(s))

