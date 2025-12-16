# Get integer
n = int(input("Please input any positive integer: "))

# Set counting values to zero
zero, odd, even = 0, 0, 0

# Check if integer is positive
if n < 0:
    print("Please follow instructions!")
    exit()
else:
    n = str(n)                  # Convert into string
    for c in n:                 # Iterate through string
        c = int(c)              # Convert string section back into integer
        if c == 0:              # If 0 add 1 to zero
            zero += 1
        elif c % 2 == 0:        # If even add 1 to even
            even += 1
        else:                   # If odd add 1 to odd
            odd += 1

# Print results
print("Zeroes: ", zero, "\nOdds: ", odd, "\nEvens: ", even)
