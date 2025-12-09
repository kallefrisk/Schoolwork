import random


# Function creating a list of n random numbers between 1-100
def random_list(n):
    lst = []
    for i in range(n):
        rn = random.randint(1, 100)
        lst.append(rn)
    return lst


# Function computing the average of the list
def average(lst):
    sum = 0
    for n in lst:
        sum += n
    return round(sum/len(lst))


# Function creating a separate list containing only
# the odd elements from the original list
def only_odd(lst):
    odd = [n for n in lst if n % 2 == 1]
    return odd


# Function concatenating list elements with a "," between
def to_string(lst):
    s = "["
    for n in lst:
        s += str(n)
        if lst.index(n)+1 < len(lst):
            s += ","
    s += "]"
    return s


# Function checking if a and b appears after each other in a list
def contains(lst, a, b):
    for c in lst:
        if c == a:
            if lst[lst.index(a)+1] == b:
                return True
    return False


# Function that checks if a list has duplicates
def has_duplicates(lst):
    for c in lst:
        t = lst.count(c)
        if t > 1:
            return True
            break
    return False
