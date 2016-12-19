def choice_sort(A):
    for i in range(0, len(A)-1):
        for k in range(i, len(A)):
            if A[k] < A[i-1]:
                A[k], A[i-1] = A[i-1],A[k]

A = [6,8,9,6,5,4,1,2,3]
choice_sort(A)
print(A)