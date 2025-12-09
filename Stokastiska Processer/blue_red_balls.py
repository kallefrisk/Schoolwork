import random as rng

pulls = 4
prob_keep_colour = 0.8  # Probability of the ball being replaced by the same color
ball_colours = {
    0: 'blue',
    1: 'red'
}

red_count = 0

simulations = 100000  # Number of simulations to run

for n in range(simulations):
    bag = [1, 1]    # Initial condition
    for _ in range(pulls):
        ball_index = rng.randint(0, 1)
        if rng.random() > prob_keep_colour:
            bag[ball_index] = 1 - bag[ball_index]   # Flip colour

    next_ball_index = rng.randint(0, 1)
    if bag[next_ball_index] == 1:
        red_count += 1

print(f'\nProbability of pulling a red ball is {red_count/simulations}\n')
