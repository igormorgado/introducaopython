# %%timeit
i = 0
r = np.zeros(len(x)-1)
while i < len(x)-1:
    r[i] = x[i+1] - x[i]
    i = i + 1
