import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math


def exact_posterior(lambda_vals):
    """Exact posterior: Gamma(alpha=5, beta=1.1)"""
    # Prior: Gamma(1, 0.1) -> shape=1, rate=0.1
    # Likelihood: Poisson(4) with rate lambda
    # Posterior: Gamma(alpha=1+4=5, rate=0.1+1=1.1)
    return stats.gamma.pdf(lambda_vals, a=5, scale=1/1.1)  # scale = 1/rate


def independence_sampler(n_samples, proposal_dist, target_log_pdf, initial_value):
    """
    Independence Metropolis-Hastings sampler
    
    Parameters:
    - n_samples: number of samples to generate
    - proposal_dist: scipy distribution object for proposals
    - target_log_pdf: function computing log of target density
    - initial_value: starting value for the chain
    """
    samples = np.zeros(n_samples)
    current = initial_value
    samples[0] = current
    accepted = 0
    
    for i in range(1, n_samples):
        # Propose new value from proposal distribution
        proposal = proposal_dist.rvs()
        
        # Calculate acceptance probability
        log_accept_ratio = (target_log_pdf(proposal) - target_log_pdf(current) + proposal_dist.logpdf(current) - proposal_dist.logpdf(proposal))
        
        # Accept or reject
        if np.log(np.random.random()) < log_accept_ratio:
            current = proposal
            accepted += 1
        
        samples[i] = current
    
    acceptance_rate = accepted / (n_samples - 1)
    return samples, acceptance_rate


def target_log_pdf(lambda_val, prior_shape=1, prior_rate=0.1, y=4):
    """
    Log of unnormalized posterior: Gamma(1,0.1) prior * Poisson(4) likelihood
    """
    if lambda_val <= 0:
        return -np.inf
    
    # Log prior: Gamma(shape=1, rate=0.1)
    log_prior = (prior_shape - 1) * np.log(lambda_val) - prior_rate * lambda_val
    
    # Log likelihood: Poisson(y=4)
    log_likelihood = 4 * np.log(lambda_val) - lambda_val - np.log(math.factorial(4))
    
    return log_prior + log_likelihood


# Tune the proposal (Exponential rate parameter)
# We want acceptance rate around 20-40% for good mixing
proposal_rates = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5]
best_rate = None
best_acceptance = 0
n_samples = 1000
burn_in = 100

print("\nTuning the Exponential proposal rate:")
for rate in proposal_rates:
    proposal_dist = stats.expon(scale=1/rate)  # scale = 1/rate
    samples, acc_rate = independence_sampler(n_samples + burn_in, proposal_dist, target_log_pdf, initial_value=1.0)
    samples = samples[burn_in:]  # Remove burn-in
    print(f"  Rate = {rate:.2f}: Acceptance rate = {acc_rate*100:.1f}%")
    
    if 0.2 <= acc_rate <= 0.4 and acc_rate > best_acceptance:
        best_rate = rate
        best_acceptance = acc_rate
        best_samples = samples

# If no rate in 20-40% range, choose closest
if best_rate is None:
    # Re-run with best performing rate
    proposal_rates = np.linspace(0.5, 3.0, 10)
    best_acc = 0
    for rate in proposal_rates:
        proposal_dist = stats.expon(scale=1/rate)
        samples, acc_rate = independence_sampler(n_samples + burn_in, proposal_dist, target_log_pdf, initial_value=1.0)
        if abs(acc_rate - 0.3) < abs(best_acc - 0.3):
            best_acc = acc_rate
            best_rate = rate
            best_samples = samples[burn_in:]

print(f"\nSelected Exponential rate = {best_rate:.2f}")
print(f"Final acceptance rate = {best_acceptance*100:.1f}%")

# Generate final samples
proposal_dist = stats.expon(scale=1/best_rate)
samples, acceptance_rate = independence_sampler(n_samples + burn_in, proposal_dist, target_log_pdf, initial_value=1.0)
samples = samples[burn_in:]  # Remove burn-in

# Plot 1: Histogram with exact density overlay
lambda_grid = np.linspace(0, 15, 1000)
exact_density = exact_posterior(lambda_grid)

# Trace plot
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# Trace plot of all samples
axes[0].plot(samples, linewidth=0.5)
axes[0].set_xlabel('Iteration')
axes[0].set_ylabel('λ')
axes[0].set_title(f'Trace Plot of λ (n={n_samples}, Acceptance Rate={acceptance_rate*100:.1f}%)')
axes[0].grid(True, alpha=0.3)

axes[1].hist(samples, bins=40, density=True, alpha=0.7, label='MCMC Samples', color='steelblue')
axes[1].plot(lambda_grid, exact_density, 'r-', linewidth=2, label='Exact Posterior (Gamma(5,1.1))')
axes[1].set_xlabel('λ')
axes[1].set_ylabel('Density')
axes[1].set_title('MCMC Approximation vs Exact Posterior')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

plt.show()
