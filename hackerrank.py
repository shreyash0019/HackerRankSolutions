import re

# Input the main string and the substring
text = input().strip()
substring = input().strip()

# Use re.finditer to find all matches of the substring in the text
matches = re.finditer(f'(?={re.escape(substring)})', text)

# Initialize a flag to check if any match is found
found = False

# Iterate through the matches and print the start and end indices
for match in matches:
    start_index = match.start()
    end_index = start_index + len(substring) - 1  # Adjust end index to be inclusive
    print((start_index, end_index))
    found = True

# If no matches were found, print (-1, -1)
if not found:
    print((-1, -1))