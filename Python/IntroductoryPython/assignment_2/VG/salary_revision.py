
# Function that calculates median of list
def median(lst):
    lst.sort()
    if len(lst) % 2 == 1:
        return lst[int(len(lst)/2)]
    else:
        a = lst[int(len(lst)/2)-1]
        b = lst[int(len(lst)/2)]
        return int((a + b)/2)


# Function that calculates average of list
def average(lst):
    sum = 0
    for n in lst:
        sum += n
    return int(sum/len(lst))


# Function that calculates max-min in list
def gap(lst):
    small = min(lst)
    large = max(lst)
    return large - small


# Input salaries in a list
s = str(input("Provide salaries separated by spaces: ")).split()

# New list of integers only
i = [int(n) for n in s]

# Print results
print("Median: ", median(i))

print("Average: ", average(i))

print("Gap: ", gap(i))
