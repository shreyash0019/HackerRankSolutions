# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : [’Red’, ’Green’, ’White’, ’Black’, ’Pink’, ’Yellow’]
# Expected Output : [’Green’, ’White’, ’Black’]


lst = ['red','green','white', 'black', 'pink','yellow']
lst.pop(0)
lst.pop(3)
lst.pop(3)
print(lst)

print("-"*50)

lst = ['red', 'green', 'white', 'black', 'pink', 'yellow']

# Take the indices from the user
indices = input("Enter the indices to remove, separated by spaces: ").split()

# Convert the input into integers
indices = [int(i) for i in indices]

# Sort indices in reverse order to avoid shifting issues
indices.sort(reverse=True)

# Remove the elements at the specified indices
for index in indices:
    lst.pop(index)

print(lst)
