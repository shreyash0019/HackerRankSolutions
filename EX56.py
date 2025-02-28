# Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

def replace_last_element_with_list(lst1, lst2):
    return lst1[:-1] + lst2

# Test case 1
print("-" * 25, "Test Case 1", "-" * 25)
test_case_1 = ([1, 3, 5, 7, 9, 10], [2, 4, 6, 8])
result_1 = replace_last_element_with_list(*test_case_1)
print("Input:", test_case_1)
print("Result:", result_1)

# Test case 2
print("-" * 25, "Test Case 2", "-" * 25)
test_case_2 = ([10, 20, 30], [40, 50])
result_2 = replace_last_element_with_list(*test_case_2)
print("Input:", test_case_2)
print("Result:", result_2)

# Test case 3
print("-" * 25, "Test Case 3", "-" * 25)
test_case_3 = (['a', 'b', 'c', 'd'], ['e', 'f', 'g'])
result_3 = replace_last_element_with_list(*test_case_3)
print("Input:", test_case_3)
print("Result:", result_3)

def replace_last_element_with_list_extend(lst1, lst2):
    lst1[-1:] = lst2
    return lst1

# Test case 1
print("-" * 25, "Test Case 4", "-" * 25)
test_case_1 = ([1, 3, 5, 7, 9, 10], [2, 4, 6, 8])
result_1 = replace_last_element_with_list_extend(*test_case_1)
print("Input:", test_case_1)
print("Result:", result_1)

# Test case 2
print("-" * 25, "Test Case 5", "-" * 25)
test_case_2 = ([10, 20, 30], [40, 50])
result_2 = replace_last_element_with_list_extend(*test_case_2)
print("Input:", test_case_2)
print("Result:", result_2)

# Test case 3
print("-" * 25, "Test Case 6", "-" * 25)
test_case_3 = (['a', 'b', 'c', 'd'], ['e', 'f', 'g'])
result_3 = replace_last_element_with_list_extend(*test_case_3)
print("Input:", test_case_3)
print("Result:", result_3)

