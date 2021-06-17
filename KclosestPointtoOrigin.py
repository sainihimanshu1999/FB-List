'''
we make max heap in this question and as heappusppop, inserts the element and then pop out minimum of them
'''
from heapq import *


def kclosestorigin(points,k):

    heap = []

    for x, y in points:
        dist = -(x*x+y*y)

        if len(heap)==k:
            heappushpop(heap,(dist,x,y))

        else:
            heappush(heap,(dist,x,y))


    return [[x,y] for dist,x,y in heap]


points = [[3,3],[5,-1],[-2,4]]
k = 2

print(kclosestorigin(points,k))
