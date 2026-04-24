import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

# Change this to complete task a and b separately.
steps = 5

# Set up the known prior and the analytical posterior
alpha_prior = 3
beta_prior = 8

trials = 10
successes = 2

alpha_posterior = alpha_prior + successes
beta_posterior = beta_prior + trials - successes

x = np.linspace(0, 1, 1000)
y_prior = stats.beta.pdf(x, alpha_prior, beta_prior)
y_posterior = stats.beta.pdf(x, alpha_posterior, beta_posterior)

# Set up the grid approximation
grid_pi = np.linspace(0, 1, steps)
grid_prior = stats.beta.pdf(grid_pi, alpha_prior, beta_prior)

grid_likelihood = grid_pi ** successes * (1 - grid_pi) ** (trials - successes)

grid_posterior = grid_prior * grid_likelihood
grid_posterior /= np.sum(grid_posterior)

# Only to display density instead of probability
grid_posterior *= steps

# Plot the results
plt.figure()
plt.plot(x, y_prior, 'r-', label=f'Prior (α={alpha_prior}, β={beta_prior})')
plt.plot(x, y_posterior, 'g-', label=f'Posterior (α={alpha_posterior}, β={beta_posterior})')
plt.bar(grid_pi, grid_posterior, width=(1/steps), label='Approximated Posterior')
plt.title('Grid Approximation')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
