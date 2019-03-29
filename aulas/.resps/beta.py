import numpy as np
import matplotlib.pyplot as plt

def betahist(axes, alfa, beta, mostras, bins=100):
    beta_sample = np.random.beta(alfa, beta, mostras)
    artista = axes.hist(beta_sample, bins, label=r"$\beta$ dist")
    titulo = axes.set_title(r"$\alpha = {}$ e $\beta = {}$".format(alfa, beta))
    axes.set_ylim(0,700)
    return artista

params = np.array([[.6, 1], [1, .6], [.5, .5], [.2, 1.2]])
samples = 10000
m, n = 2, 2

fig = plt.figure(figsize=(10,10))
grid = plt.GridSpec(m, n, fig)

ax = []
art = []

for i, (a, b) in enumerate(params):
    ax.append(fig.add_subplot(grid[i%m, i//m]))
    art.append(betahist(ax[-1], a, b, samples))


fig.suptitle(r"Figura 3: Comparação da distribuição $\beta$");

plt.savefig("imagens/fig3_gabarito.png", dpi=100)    # Salva em disco

