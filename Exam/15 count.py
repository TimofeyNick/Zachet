def count_sort(A,M):
    Q = [0]*M
    for x in A:
        Q[x] +=1
    pos = 0
    for x in range(0,M):
        for a in range(Q[x]):
            A[pos] = x
            pos +=1


#A = [6,8,9,6,5,4,1,2,3]
#M=10
#count_sort(A,M)
#print(*A)