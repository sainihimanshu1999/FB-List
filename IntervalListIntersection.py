'''
We use two pointer approach in this question
'''

def intervalIntersection(A,B):
    p1 = 0
    p2 = 0

    result = []

    while p1<len(A) and p2<len(B):
        startA,endA = A[p1]
        startB,endB = B[p2]

        if startA<=endB and startB<=endB:
            result.append([max(startA,startB),min(endA,endB)])


        if endA<=endB:
            p1+=1

        else:
            p2+=1

    return result


firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
print(intervalIntersection(firstList,secondList))
