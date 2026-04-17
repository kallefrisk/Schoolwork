import numpy as np

pi = {0.4: 0, 0.5: 0, 0.6: 0, 0.7: 0}
prior = np.array([0.10, 0.20, 0.44, 0.26])

posterior = np.array([0, 0, 0, 0])
trials = 10000

np.random.seed(1)

print(f"\nThe prior is {prior}")

for _ in range(trials):
    num = np.random.uniform()
    if num <= prior[0]:
        pi[0.4] += 1
    elif num <= np.sum(prior[0:2]):
        pi[0.5] += 1
    elif num <= np.sum(prior[0:3]):
        pi[0.6] += 1
    else:
        pi[0.7] += 1

for i, pi_idx in enumerate(pi):
    temp = np.random.binomial(n=80, p=pi_idx, size=pi[pi_idx])
    posterior[i] = np.count_nonzero(temp == 47)

print(f"\nThe posterior is now {posterior/np.sum(posterior)}\n")
