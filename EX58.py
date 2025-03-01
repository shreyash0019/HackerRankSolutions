# Write a Python program to find a tuple, the smallest second index value from a list of tuples.

# Sample list of tuples
list_of_tuples = [(1, 3), (4, 1), (6, 7), (5, 2)]

# Find the tuple with the smallest second index value
smallest_second_index_tuple = min(list_of_tuples, key=lambda x: x[1])

print("Tuple with the smallest second index value:", smallest_second_index_tuple)

print("-" * 25, "Test Case 2", "-" * 25)

# Sample list of tuples for test case 2
list_of_tuples_2 = [(10, 5), (2, 9), (8, 3), (7, 4)]

# Find the tuple with the smallest second index value
smallest_second_index_tuple_2 = min(list_of_tuples_2, key=lambda x: x[1])

print("Tuple with the smallest second index value:", smallest_second_index_tuple_2)

print("-" * 25, "Test Case 3", "-" * 25)
# Sample list of tuples
list_of_tuples = [(1, 3), (4, 1), (6, 7), (5, 2)]

# Initialize the smallest tuple
smallest_second_index_tuple = list_of_tuples[0]

# Iterate through the list of tuples to find the smallest second index value
for tuple in list_of_tuples:
    if tuple[1] < smallest_second_index_tuple[1]:
        smallest_second_index_tuple = tuple

print("Tuple with the smallest second index value:", smallest_second_index_tuple)
