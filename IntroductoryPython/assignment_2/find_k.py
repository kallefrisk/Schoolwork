# Inputting number (n)
n = int(input("Please enter a positive number: "))

# Set k1 and k2 to zero to use in for-loops
k1, k2 = 0, 0

# First check if n is positive
if n < 0:
    print("The input number must be positive!")
    exit()
else:
    #  Adding odd numbers to k1 until k1 > n
    for i in range(1, n+1, 2):
        k1 += i
        # When k1 > n print results and break the loop
        if k1 > n:
            print(f"{i} is the smallest k such that 1 + 2 + 3 + ... + k > {n}")
            break

# Adding even numbers to k2 until k2 > n
for i in range(0, n+1, 2):
    k2 += i
    # When k2 > n print the number before the last and break the loop
    if k2 > n:
        print(f"{i-2} is the largest k such that 0 + 2 + 4 + ... + k < {n}")
        break
