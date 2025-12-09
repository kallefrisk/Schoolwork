
# Set the empty list and counter
num = []
count = 0

while True:
    # Input the numbers
    n = int(input("Input any number you want."
                  + "Stop the loop by inputting a negative number. "))
    if n >= 0:
        # If the number is positive or 0; add it to the list and + 1 to counter
        num += [n]
        count += 1
    else:
        # Else break the loop
        break

# Present results
print(f"Total amount of numbers is: {count}")

print("Numbers: ", num)
