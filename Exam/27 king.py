def kolichestvo(n, m):
    """n- height, m-width"""
    K = [[0]*(m+1) for i in range (n+1)]
    K[1] = [0] + [1]*m
    for i in range(2,n+1):
        for j in range(1, m+1):
            K[i][j] =(K[i-1][j]+K[i][j-1]+K[i-1][j-1])
    return K

print(kolichestvo(5,5))


width = 3
height = 5
A = [[0]*(width) for i in range(height)]
#print(A)
