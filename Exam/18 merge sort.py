def megre_sort(A):
    if len(A)<=1:
        return A[:]
    L = megre_sort(A[:len(A)//2])
    R = megre_sort(A[len(A)//2:])
    return merge(L,R)

def merge(A,B):
    i=j=k=0
    C = [None]*(len(A) + len(B))
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C[k] = A[i]; i +=1; k +=1
        else:
            C[k] = B[j]; j +=1; k +=1
    C [k:] = A[i:] + B[j:]
    return C

A = [6,8,9,6,5,4,1,2,3]
print(megre_sort(A))