# Write a Python program to convert a pair of values into a sorted unique array.

def convert_to_sorted_unique_array(pair):

    unique_elements = list(set(pair))

    unique_elements.sort()

    return unique_elements

# Example usage
pair = (4, 2, 2, 3, 1, 4)
result = convert_to_sorted_unique_array(pair)
print(result)
