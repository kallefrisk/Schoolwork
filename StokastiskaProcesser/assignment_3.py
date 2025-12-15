import matplotlib.pyplot as plt
import random

lamda = 1
mu = 1.5
stop_time = 12
queue = 0
time = 0
time_no_customers = 0
timestamps = [0]
changes = [0]

while time < stop_time:
    arrival_time = random.expovariate(lamda)
    queue_time = random.expovariate(mu)
    if queue == 0:
        time_no_customers += min(arrival_time, queue_time)
    # if (arrival_time >= queue_time) and (queue == 0):
    #     time += arrival_time
    #     queue += 1
    #     timestamps += [time]
    #     changes += [queue]
    if arrival_time <= queue_time:
        time += arrival_time
        queue += 1
        timestamps += [time]
        changes += [queue]
    else:
        time += queue_time
        queue -= 1
        if queue < 0:
            queue = 0
        timestamps += [time]
        changes += [queue]

changes.pop(-1)

plt.stairs(changes, timestamps)
plt.xlabel('time')
plt.ylabel('# of customers')
plt.show()

print(time_no_customers/timestamps[-1], 1-lamda/mu)
