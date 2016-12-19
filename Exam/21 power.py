def pow(a,n):
    if n==0:
        return 1
    return pow(a,n-1)*a

print(pow(3,7))

def fast_power(a,n):
    """a положительное целые"""
    if n==0:
        return 1
    elif n%2==0:
        return fast_power(a**2, n//2)
    else:
        return fast_power(a,n-1)*a

#print(fast_power(4,10))