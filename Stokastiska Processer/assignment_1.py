import numpy as np
import math
import matplotlib.pyplot as plt


def poisson(k, l):
    prob = math.exp(-l)*l**k/math.factorial(k)
    return prob


def binomial(k, n, p):
    '''Binomial distribution of n tries with k successes and probability p for success'''
    prob = math.comb(n, k)*p**(k)*(1-p)**(n-k)
    return prob


def p_state(k_in, l, k_out, p, n):
    In = poisson(k_in, l)
    Out = binomial(k_out, n, p)
    return In * Out


hotel_rooms = 4             # number of states - 1
states = hotel_rooms + 1
average_families_in = 1     # poisson lamda
prob_family_out = 0.5       # binomial p
power = 20                  # number of steps in simulation

P_matrix = np.zeros((states, states))

for i in range(states):
    for j in range(states):
        for n in range(min(i, j) + 1):
            P_matrix[i, j] += p_state(j-n, average_families_in, i-n, prob_family_out, i)
    P_matrix[i, hotel_rooms] = 1 - np.sum(P_matrix[i, 0:-1])


# Compute long-run distribution with equation-system
PT_I = P_matrix.T - np.eye(states)
PT_I[-1, :] = np.ones(states)        # Replace a row with sum(pi) = 1
b = np.zeros(states)                # to force non-trivial solution
b[-1] = 1

pi = np.linalg.solve(PT_I, b)

print(f'\nπ computed numerically using equation system gives:\n{pi}')

# Compute pi using assumption long-run distribution is poisson
new_pi = np.zeros(states)
lambd = average_families_in/(1 - prob_family_out)
for i in range(len(new_pi)):
    new_pi[i] = poisson(i, lambd)
new_pi[-1] = 1 - np.sum(new_pi[:-1])

print(f'\nπ computed using poisson({lambd}) distribution gives:\n{new_pi}')

print(f'\nThe difference is thus:\n{abs(new_pi-pi)}\n')


matrices = {1: P_matrix}
Pn = np.eye(states)
for _ in range(power):
    Pn = Pn @ P_matrix
matrices[power] = Pn

for power, matrix in matrices.items():
    plt.figure(figsize=(8, 6))
    im = plt.imshow(matrix, cmap='Blues', vmin=0, vmax=1)
    cbar = plt.colorbar(im)
    cbar.set_label('Transition Probability')

    plt.xticks(range(states), [i for i in range(states)])
    plt.yticks(range(states), [i for i in range(states)])
    plt.xlabel('To State')
    plt.ylabel('From State')
    plt.title(f'Markov Chain Transition Matrix Step n = {power}')

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            plt.text(j, i, f'{matrix[i, j]:.3f}',
                     ha='center', va='center',
                     fontweight='bold')

    plt.show()
