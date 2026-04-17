import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

alpha = int(input("Alpha = "))
beta = int(input("Beta = "))

x = np.linspace(0, 1, 1000)
y = stats.beta.pdf(x, alpha, beta)

plt.figure()
plt.plot(x, y, 'r-')
plt.title(f'Beta Distribution PDF (α={alpha}, β={beta})')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True, alpha=0.3)
plt.show()
