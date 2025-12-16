from random import uniform
from math import pi


# function for approximatiing pi
def approx_pi(n):
    inside = 0
    for i in range(n):
        x = uniform(0, 1)  # Creates a point inside a 2*2 square
        y = uniform(0, 1)  # centered on origin
        if x**2 + y**2 <= 1:
            inside += 1     # Checks if point is inside circle
    pi_approx = 4*inside/n       # pi_approx = 4 * (nπ)/4 / n
    return pi_approx


# Print results
pi100 = approx_pi(100)

pi10000 = approx_pi(10000)

pi1000000 = approx_pi(1000000)

print("Approximating pi using 100 points"
      + f" is {pi100}, which is {abs(pi100-pi)} off.")

print("\nApproximating pi using 10000 points"
      + f" is {pi10000}, which is {abs(pi10000-pi)} off.")

print("\nApproximating pi using 1000000 points"
      + f" is {pi1000000}, which is {abs(pi1000000-pi)} off.")
