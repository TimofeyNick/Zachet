def big_subsequence(A):
    L = [0]*len(A)
    for i in range(len(A)):
        for j in range(i):
            if A[j] < A[i] and L[j] > L[i]:
                L[i] = L[j]
        L[i] +=1
    return max(L)

A = [3,3,5,7,9,2,1]
Sub = big_subsequence(A)
print(Sub)
