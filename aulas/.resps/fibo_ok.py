def fib(n):
    fibonacci = []
    if(n == 0):
        return fibonacci
    fibonacci.append(0)

    if(n == 1):
        return fibonacci
    fibonacci.append(1)

    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

