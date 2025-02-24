# Write a Python program to generate groups of five consecutive numbers in a list.
# Given list
lst = range(1, 11)

# Initialize an empty list to store the groups
groups = []

# Iterate through the list and create sub lists of five consecutive numbers
for i in range(len(lst) - 4):
    group = lst[i:i + 5]
    groups.append(group)

# Print the groups
for group in groups:
    print(list(group))

