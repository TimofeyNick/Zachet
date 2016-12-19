#Longest Common Subsequence
def lcs(A,B):
    n = len(A)
    m = len(B)
    L = [[0]*(m+1) for k in range(n+1)]
    for i in range(1,n+1):
        for j in range(1, m+1):
            if A[i-1]==B[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
    return L

A = [1,2,4,3,5,6]
B = [2,1,3,4,5]
print(lcs(A,B))