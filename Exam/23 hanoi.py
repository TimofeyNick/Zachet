def hanoi(n, i, k):
    """move pyramid from i to k
     n sum of blins"""
    if n==1:
        print('move blin', n ,'from', i, 'to', k)
    else:
        tmp = 6-i-k
        hanoi(n-1, i, tmp)
        print('move blin', n ,'from', i, 'to', k)
        hanoi(n-1, tmp, k)

hanoi(3,1,2)