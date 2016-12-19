def gcd(a,b):
    while a!=b:
        if a > b:
            a= a-b
        else:
            b=b-a
    return a

def gcd1(a,b):
    assert b>=0 and a>=0
    if b==0:
        return a
    return gcd1(b,a%b)

print(gcd1(100,23))