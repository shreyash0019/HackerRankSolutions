# Write a Python program to find common items from two lists.

# Input lists
lst1 = [1, 2, 3, 4, 5, 6, 10, 100]
lst2 = [1, 3, 2, 4, 5, 7, 2, 3]

common_items = []
for item in lst1:
    if item in lst2 and item not in common_items:
        common_items.append(item)

print("Common items:", common_items)

