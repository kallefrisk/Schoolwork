# Set sum to zero
sum = 0
for i in range(2, 101, 2):
    sum += i                # For every iteration add the even number to "sum"
    if i == 100:
        print("The sum of the first even number up to 100 is:", sum)
# Print results
