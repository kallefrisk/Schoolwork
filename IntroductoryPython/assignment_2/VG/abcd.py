
# A function that returns the input integer backwards
def reverse(s):
    s = str(s)
    string = ""
    for c in range(len(s)-1, -1, -1):
        letter = s[c]
        string += letter
    return int(string)


# A function that concatenates 4 entries
def get_number(a, b, c, d):
    res = str(a)+str(b)+str(c)+str(d)
    return int(res)


# Set starting values
a, b, c, d = 0, 0, 0, 0

# Four digit counter that looks for a number that is equal
# to 4 times itself, but backwards

for i in range(10):
    if a == 10:
        a = 0
    for j in range(10):
        if b == 10:
            b = 0
        for m in range(10):
            if c == 10:
                c = 0
            for n in range(10):
                if d == 10:
                    d = 0
                abcd = get_number(a, b, c, d)
                dcba = reverse(abcd)
                if abcd == 0:               # abcd = 0000: skip iteration
                    continue
                elif abcd*4 == dcba:        # Print result
                    print(f"The number {abcd} times 4 is equal to {dcba}; "
                          + "\nWhich is the same number backwards!")
                    break
                d += 1
            c += 1
        b += 1
    a += 1
