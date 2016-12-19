def hoar_soar(A):
    if len(A)<=1:
        return A[:]
    L =[]
    M = []
    R = []
    i = 0
    barrier = A[0]
    for x in A:
        i +=1
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    print(i)
    return hoar_soar(L) + M + hoar_soar(R)

A = [6,8,9,6,5,4,1,2,3]
print(hoar_soar(A))