import math as m

# Define function distance
def distance(x1, y1, x2, y2):
    dis = m.sqrt((x1-x2)**2 + (y1-y2)**2)
    return round(dis, 3)

# Get inputs for function
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

res = distance(x1, y1, x2, y2)
# Print results
print(f"The distance between ({x1},{y1}) and ({x2},{y2}) is: {res}")
