# Write a Python program to split a list based on first character of word.


lst = ['abc', 'python', 'java', 'auto']

# Dictionary to group words by their first character
grouped = {}

# Iterate through the list
for word in lst:
    first_char = word[0]  # Get the first character
    if first_char not in grouped:
        grouped[first_char] = []  # Create a new group
    grouped[first_char].append(word)  # Add the word to the group

print("Grouped words:", grouped)

