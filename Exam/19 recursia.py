def f(n):
    """вычисление целого неположительного"""
    assert n>=0
    if n==0:
        print("HC, n =", n)
        return 1
    print('ST, n =', n)
    fn_1 = f(n-1)
    result = fn_1 * n
    print('OP, n =', n)
    return result

print(f(5))

def f(n):
    assert n>=0
    if n==0:
        return 1
    return n*f(n-1)

print(f(5))
