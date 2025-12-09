import random as rng

number_of_urns = 8
dropped_balls = 9
desired_non_empty_urns = 3

results = {i+1: 0 for i in range(number_of_urns)}

simulations = 100000    # Number of simulations to run

for n in range(simulations):
    urns = {i: 0 for i in range(number_of_urns)}
    for _ in range(dropped_balls):  # Drop ball into random urn
        urns[rng.randint(0, number_of_urns - 1)] += 1
    non_empty_urns = 0
    for value in urns.values():
        if value != 0:  # Count non-empty urns
            non_empty_urns += 1
    results[non_empty_urns] += 1

print(f'\nThe probability of getting {desired_non_empty_urns} ', end='')
print(f'non-empty urns is {results[desired_non_empty_urns]/simulations}\n')
