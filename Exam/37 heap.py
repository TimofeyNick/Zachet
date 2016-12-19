from heapq import *

def heap_push(A,data):
    A.append(data)
    i = len(A)- 1
    while i !=0 and A[i]>A[(i-1)//2]:
        ip = (i-1)//2
        A[i], A[ip] = A[ip], A[i]
        i = ip

def heap_pop(A):
    result = A[0]
    i = 0
    while (2*i+1)<=len(A):
        ir = 2*i+2
        il = 2*i+1
        if ir >= len(A): #without right
            A[i]=A[il]
            return result
        if A[il] > A[ir]:
            A[il], A[i] = A[i], A[il]
            i = il
        else:
            A[ir],A[i] = A[i],A[ir]
    A[i] = A.pop()
    while i!=0 and A[i]>A[(i-1)//2]:
        ip = (i-1)//2
        A[i],A[ip] = A[ip],A[i]
        i = ip
    return result

A = [6,8,9,6,5,4,10,13]
# heapify(A)
# heappush(A,2)
# print(A)
# x = heappop(A)
# print(x)
