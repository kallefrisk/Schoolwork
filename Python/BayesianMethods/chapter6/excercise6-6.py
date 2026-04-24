import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

# Change this to complete task a and b separately.
steps = 9
end_point = 8


# Set up the known prior and the analytical posterior
s_prior = 20
r_prior = 5

samples = np.array([0, 1, 0])
n = len(samples)
outcome = np.sum(samples)

s_posterior = s_prior + outcome
r_posterior = r_prior + n

x = np.linspace(0, end_point, 1000)
y_prior = stats.gamma.pdf(x, s_prior, scale=(1 / r_prior))
y_posterior = stats.gamma.pdf(x, s_posterior, scale=(1 / r_posterior))

# Set up the grid approximation
grid_lamda = np.linspace(0, end_point, steps)
grid_prior = stats.gamma.pdf(grid_lamda, s_prior, scale=(1 / r_prior))

grid_likelihood = np.power(grid_lamda, outcome) * np.exp(-n*grid_lamda)

grid_posterior = grid_prior * grid_likelihood
grid_posterior /= np.sum(grid_posterior)

# Only to display density instead of probability
delta = steps / end_point
grid_posterior *= delta

# Plot the results
plt.figure()
plt.plot(x, y_prior, "r-", label=f'Prior (s={s_prior}, r={r_prior})')
plt.plot(x, y_posterior, "g-", label=f'Posterior (s={s_posterior}, r={r_posterior})')
plt.bar(grid_lamda, grid_posterior, width=(1/delta), label='Approximated Posterior')
plt.title('Grid Approximation')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
