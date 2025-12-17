import matplotlib.pyplot as plt
import random


def long_run_proportion(lamda, mu, n):
    return (lamda/mu)**n*(1-lamda/mu)


def expected_time_i(lamda, mu, i):
    return (1 - (mu/lamda)**(i + 1))/(lamda - mu)


lamda = 1
mu = 1.5
stop_time = 100000
queue = 0
time = 0
time_n_customers = 0
total_time_to_n_customers = 0
timestamps = [0]
queue_length = [0]
n = 0
from_k = 0
to_n = 3
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

    # Check which event happens first and update variables accordingly
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

print(f'\nFraction of time when {n} customers were in the queue: {time_n_customers/timestamps[-1]}. Expected fraction: {(lamda/mu)**n*(1-lamda/mu)}')
print(f'\nAverage time to reach {to_n} customers from {from_k} customers: {total_time_to_n_customers/times_arrived}. Expected time: {expected_time_i(lamda, mu, to_n)}\n')

plt.stairs(queue_length, timestamps, label='customers')
plt.plot(timestamps, expected_value_vector, 'r-', label='mean')
plt.xlabel('time')
plt.ylabel('# of customers')
plt.legend()
plt.show()
