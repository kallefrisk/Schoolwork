import random
# Assign aller values to countervalues and variables
n = int(input("How many number do you want? "))
nprint, all, low, high = 0, 0, 100, 0

# Check if n is positive
if n < 0:
    print("Only positive numbers please")
    exit()
else:
    # Check if loopcounter is lower than n
    while nprint < n:
        # "a" is a random number
        a = random.randint(1, 100)
        all += a
        # Add all numbers into all
        print(a, end=" ")
        nprint += 1
        # Replace the lowest number if a is lower
        if a < low:
            low = a
        # Replace highest number if a is higher
        if a > high:
            high = a
    print(f"\nThe mean is {all/n}")  # Print mean
    print(f"The highest number is {high}")  # Print highest number
    print(f"The lowest number is {low}")  # Print lowest number
