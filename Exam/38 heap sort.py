from heapq import *

def heap_sort(A):
    H = []
    for x in A:
        heappush(A, x)
    for i in H:
        A[i] = heappop(H)

A = [6,8,9,6,5,4,1,2,3]
heap_sort(A)
print(A)