def somalinha(MAT):
    m, n = MAT.shape
    r = np.zeros(m)
    for i in range(m):
        for j in range(n):
            r[i] = r[i] + MAT[i,j]

    return r
