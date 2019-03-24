a = 5
b = 2
c = 1
if (a <= c <= b) or (b <= c <= a):
    print(c)
elif abs(a - c) < abs(b - c):
    print(a)
else:
    print(b)

