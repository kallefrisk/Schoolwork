# Input the values
s = int(input("Initial savings: "))
p = int(input("Interest rate in percentage: "))
y = int(input("Number of years saving: "))

# Convert the percentage value into decimal-form
p = p * 0.01 + 1

# Compute
x = s * p**y

res = round(x)

# Display results
print("Your savings would by then amount to: ", res)
