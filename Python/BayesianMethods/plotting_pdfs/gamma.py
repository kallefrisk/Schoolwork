import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

s = float(input("S = "))
r = float(input("R = "))

x = np.linspace(0, np.max([int(r * 2) + 10, int(s * 2) + 10]), 10000)
y = stats.gamma.pdf(x, s, scale=(1 / r))

plt.figure()
plt.plot(x, y, "r-")
plt.title(f'Gamma Distribution PDF (s={s}, r={r})')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True, alpha=0.3)
plt.show()
