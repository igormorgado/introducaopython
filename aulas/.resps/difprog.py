# %%timeit
i = 0
dif_prog = np.zeros(len(x)-1)
while i < len(x)-1:
    dif_prog[i] = x[i+1] - x[i]
    i = i + 1
