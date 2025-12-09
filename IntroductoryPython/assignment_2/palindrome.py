
# Function checking if a string is a palindrome
def palindrome(s):
    # Lowercasing all cased characters
    s = s.lower()
    # New list with caracters in order
    lst = [c for c in s]
    # New list without non-letters
    word = [c for c in lst if c.isalpha()]
    # Return True or False
    return word == word[::-1]


# Palindrome??
# s = "Sir, I demand! I am a maid named Iris!"
# s = "A man, A plan, A canal; Panama!"
# s = "racecar"
s = "aibohphobia"

# Print result
print(f"Is the phrase \"{s}\" a palindrome?")

if palindrome(s):
    print(f"\nYes! The phrase \"{s}\" is a palindrome!")
else:
    print(f"\nNo! The phrase \"{s}\" is not a palindrome")
