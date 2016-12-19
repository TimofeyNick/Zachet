def fibonacci(n):
    Fib = [0,1] + [0]*(n-1)
    for i in range (2, n+1):
        Fib[i] = Fib[i-1] + Fib[i-2]
    return Fib[n]

#print(fibonacci(10))

def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)