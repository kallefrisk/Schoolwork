# Input seconds
s = int(input("Input seconds: "))

# Calculate hours and remaining seconds
h = s//3600

hres = s % 3600

# Calculate minutes and remaining seconds
m = hres//60

mres = hres % 60
s = mres

# Display results
print(h, "hours", m, "minutes", s, "seconds")
