'''
a)

The Prior model indicates that pi has a very
big chance to take on a value roughly equal to one
with a very high degree of certainty.

The Likelihood function shows that it is most
likely that pi is in the range of 0.15 to 0.3
from some collected data.

The difference seems to indikace that the prior
model is not a very good one since the collected
data seems to say otherwise.
'''

'''
b)

The Posterior model shows that the value of pi
after accounting for the collected data has shifted
the predicted pi from roughly one to somewhere
around 0.65 to 0.85.

The Posterior model aligns more closely with the
prior than the lilelihood.
'''

import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

alpha_prior, beta_prior = 30, 1
alpha_likelihood, beta_likelihood = 10, 40
alpha_posterior, beta_posterior = 150, 50


x_prior = np.linspace(0, 1, 10000)
x_likelihood = np.linspace(0, 1, 10000)
x_posterior = np.linspace(0, 1, 10000)
y_prior = stats.beta.pdf(x_prior, alpha_prior, beta_prior)
y_likelihood = stats.beta.pdf(x_likelihood, alpha_likelihood, beta_likelihood)
y_posterior = stats.beta.pdf(x_posterior, alpha_posterior, beta_posterior)


plt.figure()
plt.plot(x_prior, y_prior, 'y-')
plt.plot(x_likelihood, y_likelihood, "b-")
plt.plot(x_posterior, y_posterior, 'g-')
plt.title(f'Beta_prior Distribution PDF (α={alpha_prior}, β={beta_prior})')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True, alpha=0.3)
plt.show()
