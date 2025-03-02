# Write a Python program to insert a given string at the beginning of all items in a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : [’emp1’, ’emp2’, ’emp3’, ’emp4’]

# Given list and string
sample_list = [1, 2, 3, 4]
s = "emp"

# Create a new list with the string inserted at the beginning of each item
new_list = [s + str(item) for item in sample_list]

# Print the result
print(new_list)

