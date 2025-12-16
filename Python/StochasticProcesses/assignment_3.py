import matplotlib.pyplot as plt
import random

def long_run_proportion(lamda, mu, n):
    return (lamda/mu)**n*(1-lamda/mu)


lamda = 1
mu = 1.3
stop_time = 100
queue = 0
time = 0
time_n_customers = 0
timestamps = [0]
queue_length = [0]
n = 0

while time < stop_time:
    arrival_time = random.expovariate(lamda)
    queue_time = random.expovariate(mu)
    if queue == n:
        time_n_customers += min(arrival_time, queue_time)
    # if (arrival_time >= queue_time) and (queue == n):
    #     time += arrival_time
    #     queue += 1
    #     timestamps += [time]
    #     queue_length += [queue]
    if arrival_time <= queue_time:
        time += arrival_time
        queue += 1
        timestamps += [time]
        queue_length += [queue]
    else:
        time += queue_time
        queue -= 1
        if queue < 0:
            queue = 0
        timestamps += [time]
        queue_length += [queue]

queue_length.pop(-1)
timestamps[-1] = stop_time

expected_value = 0
for i in range(max(queue_length)):
    expected_value += i * long_run_proportion(lamda, mu, i)

print(expected_value)

plt.stairs(queue_length, timestamps, label='customers')
plt.plot(timestamps, [expected_value for _ in range(len(timestamps))], 'r-', label='mean')
plt.xlabel('time')
plt.ylabel('# of customers')
plt.legend()
plt.show()

print(time_n_customers/timestamps[-1], (lamda/mu)**n*(1-lamda/mu))
