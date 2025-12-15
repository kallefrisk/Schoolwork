import matplotlib.pyplot as plt
import random

lamd = 0.75
mu = 1
stop_time = 4
queue = 0
time = 0
queue_data = []

while time < stop_time:
    arrival_time = random.expovariate(lamd)
    time += arrival_time
    queue_data += [(time, 1)]

time = 0
while time < stop_time:
    queue_time = random.expovariate(mu)
    time += queue_time
    queue_data += [(time, -1)]

edges = []
values = []
for k in queue_data:
    edges += [k[0]]
    values += [k[1]]
edges += [stop_time]

print(edges, values)
plt.stairs(edges, values)
plt.show()