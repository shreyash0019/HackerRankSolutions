def flatten_shallow_list(nested_list):
    # List comprehension to flatten the shallow list
    return [item for sublist in nested_list for item in sublist]


# Example shallow list
shallow_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = flatten_shallow_list(shallow_list)

print("Original Shallow List:", shallow_list)
print("Flattened List:", flattened_list)
