A = [1,2,3,4,5,6,7,8]
N = 8
tmp = A[-1]
for i in range(N-1,0,-1):
    A[i]=A[i-1]
A[0] = tmp
print(*A)