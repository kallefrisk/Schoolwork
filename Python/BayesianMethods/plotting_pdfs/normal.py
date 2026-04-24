import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

mu = float(input("Mu = "))
sigma = float(input("Sigma = "))

x = np.linspace(mu - 5 * sigma, mu + 5 * sigma, 10000)
y = stats.norm.pdf(x, mu, sigma)

plt.figure()
plt.plot(x, y, 'r-')
plt.title(f'Normal Distribution PDF (μ={mu}, $σ^2$={sigma})')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True, alpha=0.3)
plt.show()
