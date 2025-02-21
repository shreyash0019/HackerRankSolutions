# Write a Python program to change the position of every n-th value with the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]


def swap_adjacent(lst):
    # Iterate through the list in steps of 2
    for i in range(0, len(lst) - 1, 2):
        # Swap the current element with the next element
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

# Sample list
sample_list = [0, 1, 2, 3, 4, 5]

# Swap adjacent values
result = swap_adjacent(sample_list)

print("Expected Output:", result)
