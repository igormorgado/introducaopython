# %%timeit
i = 0
dif_prog = np.zeros(len(fibo)-1)
while i < len(fibo)-1:
    dif_prog[i] = fibo[i+1] - fibo[i]
    i = i + 1
