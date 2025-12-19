import matplotlib.pyplot as plt
import random
import math as m
import numpy as np


def long_run_proportion(lamda, mu, n):
    return (lamda/mu)**n*(1-lamda/mu)


def expected_time_i_queue(lamda, mu, i):
    return (1 - (mu/lamda)**(i + 1))/(lamda - mu)


def rate_leaving(lamda, mu, n):
    return (n + 1)*lamda + n*mu


def expected_time_i_wolves(lamda, mu, n):

    matrix = (-1)*np.eye(n)
    b = np.zeros((n, 1))

    for i in range(n):
        for j in range(n):
            if j == (i - 1):
                matrix[i][j] = i*mu/rate_leaving(lamda, mu, i)
            elif j == (i + 1):
                matrix[i][j] = (i + 1)*lamda/rate_leaving(lamda, mu, i)
        b[i] = -1/rate_leaving(lamda, mu, i)

    result_vector = np.linalg.solve(matrix, b)

    return result_vector[0][0]


# PROBLEM 1

lamda = 1
mu = 1.5
stop_time = 100000
n = 0
from_k = 0
to_n = 3

queue = 0
time = 0
time_n_customers = 0
total_time_to_n_customers = 0
timestamps = [0]
queue_length = [0]
coming_from_k = False
times_arrived = 0

while time < stop_time:
    arrival_time = random.expovariate(lamda)
    queue_time = random.expovariate(mu)

    # Add time to count how long we spend in state n
    if queue == n:
        time_n_customers += min(arrival_time, queue_time)

    # Start the timer to count time from state k to state n
    if queue == from_k and not coming_from_k:
        time_to_n_customers = 0
        coming_from_k = True

    # Record time taken from state k to state n
    elif queue == to_n and coming_from_k:
        total_time_to_n_customers += time_to_n_customers
        times_arrived += 1
        coming_from_k = False

    # Check which event happens first and update queue accordingly
    if arrival_time <= queue_time:
        queue += 1
    else:
        queue -= 1

    # Make sure queue stays non-negative
    if queue < 0:
        queue = 0

    shorter_time = min(arrival_time, queue_time)
    time += shorter_time
    timestamps += [time]
    queue_length += [queue]
    time_to_n_customers += shorter_time

queue_length.pop(-1)
timestamps[-1] = stop_time

expected_value = 0
for i in range(max(queue_length)):
    expected_value += i * long_run_proportion(lamda, mu, i)

expected_value_vector = [expected_value for _ in range(len(timestamps))]

print('\n                        --------  Problem 1  --------')
print(f'\nFraction of time when {n} customers were in the queue: {time_n_customers/timestamps[-1]}. Expected fraction: {long_run_proportion(lamda, mu, n)}.')
print(f'\nThe average amount of customers in the queue: {expected_value}. Expected average: {lamda/(mu-lamda)}.')
print(f'\nAverage time to reach {to_n} customers from {from_k} customers: {total_time_to_n_customers/times_arrived}. Expected time: {expected_time_i_queue(lamda, mu, to_n)}.\n')

plt.figure(1, [16, 8])
plt.subplot(1, 2, 1)
plt.stairs(queue_length, timestamps, label='customers')
plt.plot(timestamps, expected_value_vector, 'r-', label='mean')
plt.xlabel('time')
plt.ylabel('# of customers')
plt.legend()


# PROBLEM 2

theta = lamda
wolves = 0
time = 0
timestamps = [0]
wolf_population = [0]
total_time_to_n_wolves = 0
time_n_wolves = 0
coming_from_k = False
times_arrived = 0

while time < stop_time:
    immigration_time = random.expovariate(theta)

    birth_times = [random.expovariate(lamda) for _ in range(wolves)]
    birth_time = min(birth_times) if len(birth_times) > 0 else 1e100

    death_times = [random.expovariate(mu) for _ in range(wolves)]
    death_time = min(death_times) if len(death_times) > 0 else 1e100

    shorter_time = min(immigration_time, birth_time, death_time)

    # Add time to count how long we spend in state n
    if wolves == n:
        time_n_wolves += shorter_time

    # Start the timer to count time from state k to state n
    if wolves == from_k and not coming_from_k:
        time_to_n_wolves = 0
        coming_from_k = True

    # Record time taken from state k to state n
    elif wolves == to_n and coming_from_k:
        total_time_to_n_wolves += time_to_n_wolves
        times_arrived += 1
        coming_from_k = False

    # Check which event happens first and update wolves accordingly
    if shorter_time == immigration_time:
        wolves += 1

    elif shorter_time == birth_time:
        wolves += 1

    else:

        wolves -= 1

    # Make sure wolves stays non-negative
    if wolves < 0:
        wolves = 0

    time += shorter_time
    time_to_n_wolves += shorter_time
    timestamps += [time]
    wolf_population += [wolves]

wolf_population.pop(-1)
timestamps[-1] = stop_time

expected_value = 0
for i in range(max(queue_length)):
    expected_value += i * long_run_proportion(lamda, mu, i)

expected_value_vector = [expected_value for _ in range(len(timestamps))]

print('\n                        --------  Problem 2  --------')
print(f'\nFraction of time when {n} amount of wolves were in the preserve: {time_n_wolves/stop_time}. Expected fraction: {long_run_proportion(lamda, mu, n)}.')
print(f'\nThe average number of wolves in the preserve: {expected_value}. Expected average: {lamda/(mu-lamda)}.')
print(f'\nAverage time to reach {to_n} wolves from {from_k} wolves: {total_time_to_n_wolves/times_arrived}. Expected time: {expected_time_i_wolves(lamda, mu, to_n)}.\n')

plt.subplot(1, 2, 2)
plt.stairs(wolf_population, timestamps, label='wolves')
plt.plot(timestamps, expected_value_vector, 'r-', label='mean')
plt.xlabel('time')
plt.ylabel('wolves')
plt.legend()
plt.show()
