import numpy as np
from matplotlib import pyplot as plt

samples = np.array([12, 12, 12, 0])
sum_samples = np.sum(samples)
num_samples = len(samples)

x = np.linspace(0, 20, 1000)
y = np.power(x, sum_samples) * np.exp(- num_samples * x)

plt.figure()
plt.plot(x, y, "r-")
plt.title(f'Poisson likelihood')
plt.xlabel('x')
plt.ylabel('Relative Probability')
plt.grid(True, alpha=0.3)
plt.show()
