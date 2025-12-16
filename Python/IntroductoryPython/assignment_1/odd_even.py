# Read input
n = int(input("Odd or Even? "))

# Check if divisible by 7, even or odd
if n % 7 == 0:
    print("divisible by seven!")
elif n % 2 == 0:
    print("Even!")
elif n % 2 == 1:
    print("Odd!")
