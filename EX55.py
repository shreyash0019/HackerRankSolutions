# Write a Python program to check if all items of a given list of strings is equal to a given string.
print("-"*25, "test-case 1", "-"*25)
lst = ['a','b','c','d','e']
coca = ''.join(lst)
st = 'abced'
if coca == st:
    print("Both Are same")
else:
    print("Both Are Different")

print("-"*25, "test-case 2", "-"*25)
# Sample data
lst = ['a', 'b', 'c', 'd', 'e']
st = 'edcba'  # Shuffled version of the list elements

# Sort the list and the string
sorted_lst = sorted(lst)
sorted_st = ''.join(sorted(st))

# Check if sorted list and sorted string are equal
if sorted_lst == sorted_st:
    print("Both have the same elements (ignoring order)")
else:
    print("Both have different elements")

print("-"*25, "test-case 3", "-"*25)
lst = ['a', 'b', 'c', 'd', 'e']
st = 'abced'

# Check if concatenation of list elements is equal to the given string
if ''.join(lst) == st:
    print("Both Are same")
else:
    print("Both Are Different")


print("-" * 25, "test-case 4", "-" * 25)

# Additional checks for other test cases, if needed
lst2 = ['a', 'b', 'c', 'd', 'e']
st2 = 'abcde'  # Modified string to match lst2

if ''.join(lst2) == st2:
    print("Both Are same")
else:
    print("Both Are Different")
