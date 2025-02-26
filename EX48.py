#Write a Python program to sort a list of nested dictionaries.
# my_collection = {
# ’KEY1’:{’name’:’foo’,’data’:1351,’completed’:100},
# ’KEY2’:{’name’:’bar’,’data’:1541,’completed’:12},
# ’KEY3’:{’name’:’baz’,’data’:58413,’completed’:18}
# }
# sorted_keys = sorted(my_collection, key=lambda x: (my_collection[x][’completed’]))
# print(sorted_keys)

my_collection = {
    'KEY1': {'name': 'foo', 'data': 1351, 'completed': 100},
    'KEY2': {'name': 'bar', 'data': 1541, 'completed': 12},
    'KEY3': {'name': 'baz', 'data': 58413, 'completed': 18}
}

# Sorting based on the 'completed' key in each nested dictionary
sorted_keys = sorted(my_collection, key=lambda x: my_collection[x]['completed'])

# Printing the sorted keys
print(sorted_keys)

# If you want a sorted dictionary, use:
sorted_dict = {k: my_collection[k] for k in sorted_keys}
print(sorted_dict)
