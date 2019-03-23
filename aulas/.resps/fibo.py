a, b, i = 0, 1, 2
fibo = [a, b]
while i < 100:
    i = i + 1
    a, b = b, a+b
    fibo.append(b)
