# Input positive odd number
n = int(input("Please enter a positive number: "))

# Check if number is odd and positive
if n < 0:
    print("Follow instructions!")
    exit()
else:
    # Print out statement before the for-loop
    print("All odd using for:", end=" ")
    for i in range(1, n+1, 2):
        print(i, end=" ")

print()

odd = 1
# Print statement before the while loop
print("All odd using while:", end=" ")
while odd <= n:
    print(odd, end=" ")
    odd += 2
