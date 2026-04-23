import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

plots = int(input("Enter the amount of plots = "))

parameters = {}
for i in range(plots):
    alpha = float(input(f"Alpha_{i+1} = "))
    beta = float(input(f"Beta_{i+1} = "))
    parameters[i] = (alpha, beta)

x = np.linspace(0, 1, 10000)

plt.figure()
for i, values in enumerate(parameters.values()):
    alpha = values[0]
    beta = values[1]
    plt.subplot(len(parameters) // 5 + 1, 3, i + 1)
    y = stats.beta.pdf(x, alpha, beta)
    plt.plot(x, y)
    plt.title(f'α={alpha}, β={beta}')
plt.suptitle(f'Beta Distribution PDF')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True, alpha=0.3)
plt.show()
