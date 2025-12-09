
import random

# Recieving a random number
n1 = random.randint(-10, 10)

print("The generated number is:", n1)

# Checking if n1 is zero
if n1 == 0:
    print(n1, "is even and neither positive nor negative")
elif n1 != 0:
    # Checking if n1 is even
    if n1 % 2 == 0:
        # Checking if n1 is positive
        if n1 > 0:
            print(n1, "is even and positive")
        else:
            # If n1 isn't positive, it's negative
            print(n1, "is even and negative")
    else:
        # If n1 isn't even, it's odd
        if n1 > 0:
            # Checking if n1 is positive
            print(n1, "is odd and positive")
        else:
            # If n1 isn't positive, it's negative
            print(n1, "is odd and negative")

n2 = random.randint(-10, 10)

print("\nThe generated number is:", n2)

# The rest is a copy-paste from above
if n2 == 0:
    print(n2, "is even and neither positive nor negative")
elif n2 != 0:
    if n2 % 2 == 0:
        if n2 > 0:
            print(n2, "is even and positive")
        else:
            print(n2, "is even and negative")
    else:
        if n2 > 0:
            print(n2, "is odd and positive")
        else:
            print(n2, "is odd and negative")
