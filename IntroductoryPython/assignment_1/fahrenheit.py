# Get temperature in fahrenheit
f = float(input("Enter temperature in fahrenheit: "))

# Calculate celcius
c = (f - 32) / (9 / 5)

# Rounding
res = round(c, 2)

# Present result
print("The corresponding temperature is:", res, "Celcius")
