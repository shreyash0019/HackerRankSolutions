# Write a Python program to remove key values pairs from a list of dictionaries

# Sample list of dictionaries
list_of_dicts = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
]

# Key(s) to be removed
keys_to_remove = ['age']

# Remove specified key(s) from each dictionary
for d in list_of_dicts:
    for key in keys_to_remove:
        if key in d:
            del d[key]

# Print the updated list of dictionaries
print(list_of_dicts)
