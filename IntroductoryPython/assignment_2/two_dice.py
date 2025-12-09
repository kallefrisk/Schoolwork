from random import randint


# Function for counting n in x
def x(n):
    global res
    return res.count(n)


# Set empty list
res = []

for i in range(10000):
    # Create 10000 dice throws and add the results to res
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    res.append(dice1 + dice2)

# Print results
print("Frequency table (sum,count) for rolling two dices 10000 times")

# Print results in an ordered manner
print("\n2\t", x(2), "\n3\t", x(3), "\n4\t", x(4), "\n5\t", x(5),
      "\n6\t", x(6), "\n7\t", x(7), "\n8\t", x(8), "\n9\t", x(9),
      "\n10\t", x(10), "\n11\t", x(11), "\n12\t", x(12))
