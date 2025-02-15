# Write a Python program to get the difference between the two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Difference (List1 - List2)
difference_1_to_2 = [x for x in list1 if x not in list2]

# Difference (List2 - List1)
difference_2_to_1 = [x for x in list2 if x not in list1]

print("Difference (List1 - List2):", difference_1_to_2)
print("Difference (List2 - List1):", difference_2_to_1)
