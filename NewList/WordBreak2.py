'''
wordBreak with whole path 
'''

def wordBreak2(s,wordDict):
    memo = {}
    def dfs(s):
        if s in memo:
            return memo[s]

        result = []

        for word in wordDict:
            if s[:len(word)] == word:
                if len(s) == len(word):
                    result.append(word)

                else:
                    suffix = s[len(word):]
                    temp = dfs(suffix)
                    for t in temp:
                        result.append(word+' '+t)

        memo[s] = result
        return memo[s]

    return dfs(s)


s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]

print(wordBreak2(s,wordDict))