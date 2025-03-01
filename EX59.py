# Write a Python program to create a list of empty dictionaries

# Prompt the user for the number of empty dictionaries to create
n = int(input("Enter the number of empty dictionaries to create: "))

# Create a list of empty dictionaries
list_of_empty_dicts = [{} for i in range(n)]

# Print the result
print(list_of_empty_dicts)
print("-"*25, "2nd-method", "-"*25)

# Prompt the user for input in the format key: value
n = input("Enter the items of the dictionary in key: value pairs separated by commas: ")

# Split the input into individual pairs and create the dictionary
items = n.split(",")
res = {item.split(":")[0].strip(): item.split(":")[1].strip() for item in items}

# Print the result
print(res)

