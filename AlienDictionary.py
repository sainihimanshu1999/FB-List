'''
In this question we have to check wheter the words are sorted in custom order that is given, for this we have use
dictionary
'''

def aliendict(words,order):
    dic = {c:i for i,c in enumerate(order)}

    for i in range(len(words)-1):
        for j in range(len(words[i])):

            if j>=len(words[i+1]):
                return False

            
            if words[i][j] != words[i+1][j]:
                if dic[words[i][j]]>dic[words[i+1][j]]:
                    return False
                break



    return True


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

print(aliendict(words,order))