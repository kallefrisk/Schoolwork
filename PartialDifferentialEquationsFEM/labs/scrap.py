import random
import matplotlib.pyplot as plt

games = 20

accuracy = 0.1

results = {}

for i in range(games):
    throws = 0
    balls = 4
    while balls > 0:
        throws += 1
        throw = random.random()
        if throw <= accuracy:
            balls += 4
        else:
            balls -= 1
        
    results[i] = throws

plt.figure(1)
plt.bar(results.keys(), results.values())
plt.show()
