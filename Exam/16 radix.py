def redix_sort(A):
    M = len(str(max(A)))
    for k in range(0, M):
        B = [[] for i in range (10)]
        for x in A:
            digit = x//(10**k)%10
            B[digit].append(x)
        A[:] = B[0]+B[1]+B[2]+B[3]+B[4]+B[5]+B[6]+B[7]+B[8]+B[9]

A = [60,84,9112,645,5,41,1123,25,0]
redix_sort(A)
print(*A)