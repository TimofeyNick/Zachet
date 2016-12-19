def stoimost(n,Price):
    C = [float('inf'), Price[1]] + [None]*(n-1)
    for i in range(2, n+1):
       C[i] = Price[i] + min(C[i-1],C[i-2])
    return C

def shortest_path(n,Coasts):
    path = [n]
    while path[-1]!= 1:
        k = path[-1]
        if Coasts[k-1]<Coasts[k-2]:
            path.append(k-1)
        else:
            path.append(k-2)
    path[:] = path[::-1]
    return path


n = 6
#Price = [None] +[int() for i in input().split()]
Price = [None, 2,3,4,5,6,7]
Coasts = stoimost(n,Price)
print(Coasts[n])
Path = shortest_path(n, Coasts)
print(*Path)