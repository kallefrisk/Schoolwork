id = str(input("Enter a chess square identifier (e.g. e5): "))                  # Input square identifier

n1 = str(id[0])                                                                 # Separate the letter and number into variables
n2 = int(id[1])

if n1 in ["a","b","c","d","e","f","g","h"]:
    if n1 in ["a","c","e","g"]:                                                 # Compute the squares color
        if n2 in [2,4,6,8]:
            res = "white"
        elif n2 in [1,3,5,7]:
            res = "black"
        else:
            res = "not on the board!"                                           # (1) Should n1 or n2 be outside the,
    elif n1 in ["b","d","f","h"]:                                               # (2) boundaries of a-h and 1-8 respectively
        if n2 in [2,4,6,8]:                                                     # (3) results will be a square outside the board
            res = "black"
        elif n2 in [1,3,5,7]:
            res = "white"
        else:
            res = "not on the board!"
else:
    res = "not on the board!"

print("The square is", res)                                                     # Print results