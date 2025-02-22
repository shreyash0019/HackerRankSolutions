# write a Python program to create multiple lists.

# Number of lists to create
num_lists = 3

# Initialize a dictionary to hold the lists
list_dict = {}

# Create lists dynamically
for i in range(1, num_lists + 1):
    list_name = f"list_{i}"  # Generate a name for each list
    list_dict[list_name] = []  # Create an empty list

# Add some example data to each list
for name in list_dict:
    list_dict[name].extend(range(1, 6))  # Add numbers 1 to 5 to each list

# Print all the lists
for name, lst in list_dict.items():
    print(f"{name}: {lst}")
