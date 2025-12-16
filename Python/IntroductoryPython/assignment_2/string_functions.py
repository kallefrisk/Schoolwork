
# A function that concatenates a string n times
def concat(s, n):
    con = ""
    for i in range(n):
        con += s
    return con


# A function that counts how many times x appears in s
def count(s, x):
    sum = 0
    for c in s:
        if c == x:
            sum += 1
    return sum


# A function that writes a string bacwards
def reverse(s):
    string = ""
    for c in range(len(s)-1, -1, -1):
        letter = s[c]
        string += letter
    return string


# A function that returns the first and last characters of a string
def first_last(s):
    length = len(s)
    a = s[0]
    b = s[length-1]
    return a, b


# A function that checks if a string contains two "X"
def has_two_X(s):
    Xes = 0
    for c in s:
        if c == "X":
            Xes += 1
    return True if Xes == 2 else False


# A function that checks if a character appears twice or more in a string
def has_duplicates(s):
    duplicate = False
    for i in range(len(s)):
        s[i]
        for j in range(len(s)):
            if i < j:
                if s[j] == s[i]:
                    duplicate = True
                    break
        if duplicate:
            break
    return duplicate
