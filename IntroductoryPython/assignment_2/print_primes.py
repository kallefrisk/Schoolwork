
# Input integer for n
n = int(input("How many primes do you want to see?  "))

# Set starting values
start = 1
nprint = 1

# Check if positive
if n < 0:
    print("Idiot!")
    exit()
elif n == 0:
    exit()
else:
    print(2, end=" ")       # Reason why nprint starts at 1
    while nprint < n:       # Stop loop when n primes have been printed
        start += 2
        for i in range(2, start):   # Check if prime
            prime = True
            if start % i == 0:
                prime = False
                break
        if prime:
            print(start, end=" ")   # If prime; Print results
            nprint += 1             # When nprint == n; loop stops
            if nprint % 10 == 0:    # Line break every ten primes
                print()
