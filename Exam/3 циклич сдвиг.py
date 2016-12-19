A = [1,2,3,4,5,6,7,8]
N = 8
tmp = A[0]
for i in range(N-1):
    A[i]=A[i+1]

A[-1] = tmp
print(*A)
