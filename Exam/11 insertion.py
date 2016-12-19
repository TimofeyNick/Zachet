def fool_sort(A):
    for k in range(1,len(A)):

        i = 0
        while i < len(A)-1:
            if A[k-1] > A[k]:
                A[k-1],A[k] = A[k-1],A[k]
                i = 0
            else:
                i +=1

A = [6,8,9,6,5,4,1,2,3]
fool_sort(A)
print(*A)