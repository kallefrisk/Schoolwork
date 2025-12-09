from random import randint

# Input variables
k = int(input("Size of raft: "))

st = int(input("Amount of steps: "))

sa = int(input("Number of sailors: "))

# Counting variables
up = 0
left = 0
down = 0
right = 0
ove = 0
# Iterate for each sailor
for n in range(sa):
    # Iterate steps for each sailor
    for i in range(st):
        rn = randint(1, 4)
        if rn == 1:
            up += 1
        elif rn == 2:
            left += 1
        elif rn == 3:
            down += 1
        else:
            right += 1
        # Check if sailor is overboard
        if up-down not in range(-k, k+1):
            ove += 1
            break
        elif left-right not in range(-k, k+1):
            ove += 1
            break
    # Reset counters
    up = 0
    left = 0
    down = 0
    right = 0

# Print results
res = round((ove/sa)*100, 2)

print(f"Out of {sa} drunk sailors, {ove} ({res}%) fell into the water.")
