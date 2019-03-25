import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font',**{'family':'serif','serif':['Palatino']})

plt.rc('text', usetex=True)

x = np.linspace(-4.49, 3.49, 101)
a, b, c = 1, 1, -2
y = a*x**2 + b*x + c

fig = plt.figure(figsize=(5,4))
gs = plt.GridSpec(1,1, figure=fig)
ax = fig.add_subplot(gs[0, 0])
ax.plot(x, y, label='$f(x) = x^2 + x - 2$')
ax.scatter([-2, 1],[0, 0], color='red', label='raízes')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set(xlabel='$x$', ylabel='$f(x)$')
ax.xaxis.set_label_coords(0.94, 0.16 )
ax.yaxis.set_label_coords(.48, 0.92 )
ax.grid(color='black', linestyle='--', alpha=.05)
leg = ax.legend(loc=9, bbox_to_anchor=(0.5,0), ncol=2)
plt.title('Figura 1: Parábola em $[-4, 3]$');
plt.savefig('../imagens/parabola.png',dpi=150, bbox_extra_artists=(leg,), bbox_inches='tight')
