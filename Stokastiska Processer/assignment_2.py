import random
import math
import numpy as np

# Problem 1

desk_lambda = [1, 1]
simulations = 10000
smith_last = 0
smith_time = 0

for _ in range(simulations):
    time_desk_1 = random.expovariate(desk_lambda[0])
    time_desk_2 = random.expovariate(desk_lambda[1])
    if time_desk_1 <= time_desk_2:
        time_smith = random.expovariate(desk_lambda[0])
        total_time = time_desk_1 + time_smith
        smith_time += time_smith + time_desk_1
        if total_time > time_desk_2:
            smith_last += 1
    else:
        time_smith = random.expovariate(desk_lambda[1])
        total_time = time_desk_2 + time_smith
        smith_time += time_smith + time_desk_2
        if total_time > time_desk_1:
            smith_last += 1

smith_last_percentage = smith_last / simulations
smith_time_mean = smith_time / simulations
expected_smith_time = 3 / (desk_lambda[0] + desk_lambda[1])

print('\n----Results For Problem 1.----')
print(f'\nFraction of time Smith was last: {smith_last_percentage}\n')
if desk_lambda[0] == desk_lambda[1]:
    print(f'Expected fraction of time smith was last: {0.5}\n')
print(f'Expected time in office: {expected_smith_time}\n')
print(f'Time Smith was in office: {smith_time_mean}\n')


# Problem 2

def claim_cost(discount, time, cost):
    return np.exp(-discount*time)*cost


alpha = 0.5
lamd = 10
mu = 1
stop_time = 100000
simulations = 10
total_cost = 0

for _ in range(simulations):
    time = 0
    claims = 0
    while time < stop_time:
        time += random.expovariate(lamd)
        cost = random.expovariate(1/mu)
        total_cost += claim_cost(alpha, time, cost)
        claims += 1

expected_cost = lamd*mu*(1-np.exp(-alpha*stop_time))/alpha
sample_mean = total_cost / simulations

print('\n----Results For Problem 2.----\n')
print(f'Expected cost: {expected_cost}, Average total cost is {sample_mean}\n')
print(f'Expected D(t) = {lamd*mu*stop_time}, Simulated D(t) = {sample_mean}\n')
print(f'Expected D(t)/t = {lamd*mu*stop_time/stop_time}, Simulated D(t)/t = {sample_mean/stop_time}\n')
