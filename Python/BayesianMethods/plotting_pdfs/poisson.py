import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

lamda = float(input("Lambda = "))

x = np.array([i for i in range(int(lamda * 2 + 10))])
y = stats.poisson.pmf(x, lamda)

plt.figure()
plt.bar(x, y)
plt.title(f'Poisson Distribution PDF (λ={lamda})')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True, alpha=0.3)
plt.show()
