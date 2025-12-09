# Input three digit number
x = int(input("input three digit number: "))

# Compute 1:st (a), 2:nd (b) and 3:rd (c) digits
a = x//100

b = (x % 100)//10

c = ((x % 100) % 10)

# Add the digits
res = a + b + c

# Display results
print(res)
