def fool_sort(A):
    i = 0
    while i < (len(A)-1):
        if A[i] > A[i+1]:
            A[i],A[i+1] = A[i+1],A[i]
            i = 0
        else:
            i +=1
