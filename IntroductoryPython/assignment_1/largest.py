
a = int(input("A="))
b = int(input("B="))                        # Recieve inputs
c = int(input("C="))


if a > b and a > c:                         # Check if A is biggest
    katt = a
elif b > c and b > a:                       # Check if B is biggest
    res = b
elif c > a and c > b:                       # Check if C is biggest
    res = c
elif a == b and a > c:                      # Check if A AND B are the biggest
    res = "A and B", a, b
elif b == c and b > a:                      # Check if B AND C are the biggest
    res = "B and C", b, c
elif a == c and a > b:                      # Check if A AND C are the biggest
    res = "A and C", a, c
else:
    res = "All three integers are the same"

print("The largest integer is:", res)           # Print the results
