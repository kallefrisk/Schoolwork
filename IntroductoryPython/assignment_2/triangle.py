
n = int(input("Please input a positive odd integer: "))


if n < 0 or n % 2 == 0:
    print("Enter a positive and odd number please!")
    exit()
else:
    # Right angled triangle
    for i in range(n, 0, -1):  # Start at n and go down in size
        stars = ("*")*i
        print((n-i)*" ", stars)

print()

# Isosceles triangle
for i in range(1, n+1, 2):  # i is only odd numbers
    stars = ("*")*i
    space = " " * int((n-i)/2)
    print(space, stars)
