# %%timeit
i = 0
pt_med = np.zeros(len(x)-1)
while i < len(x)-1:
    pt_med[i] = (x[i+1] - x[i])/2
    i = i + 1
