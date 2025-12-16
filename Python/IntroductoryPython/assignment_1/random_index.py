import random

s = str(input("Here: "))

sz = len(s)

index = random.randint(0, sz-1)
print(s[index], index)
