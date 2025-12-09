import random

# Get random number
n = random.randint(1, 100)

# Max number of guesses
max_g = 10

# Loop which tells if "n" is higher or lower than the input guess
for guesses in range(1, max_g+1):
    guess = int(input("Guess between 1-100: "))
    print(f"Number of guesses: {guesses}")
    if guess > n:                   # If guess is lower than "n"
        print("Lower")
        continue
    elif guess < n:                 # If guess is higher than "n"
        print("Higher")
        continue
    else:                           # Comments depending on amount of guesses
        if guesses == 1:
            print("CORRECT! Always lucky!")
        elif guesses == 2:
            print("Very lucky! Correct!")
        elif guesses == 3:
            print("Correct! Very, VERY good job!")
        elif guesses == 4:
            print("Remarkable job! That's correct!")
        elif guesses == 5:
            print("Five tries is good!")
        else:
            print("You guessed it right.")
        break                       # Break the loop on correct guess
else:
    print("Out of guesses! Try again!")        # Result if out of guesses
