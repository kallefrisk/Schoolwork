from random import randint

# Set empty list
lotto = []

# Add numbers to list
while len(lotto) < 7:
    rn = randint(1, 35)
    # Check if number already in list
    if rn in lotto:
        continue
    else:
        lotto.append(rn)

# Sort list
lotto.sort()

# Print result
print(lotto)
