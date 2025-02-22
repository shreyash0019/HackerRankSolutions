# Write a Python program to find missing and additional values in two lists.
# Sample data : Missing values in second list: b,a,c

def find_missing_and_additional_values(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    missing_values = set1 - set2
    additional_values = set2 - set1

    return missing_values, additional_values


# Sample data
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = ['d', 'e', 'f']


missing_values, additional_values = find_missing_and_additional_values(list1, list2)

print("Missing values in second list:", missing_values)
print("Additional values in second list:", additional_values)
