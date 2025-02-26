# 51. Write a Python program to split a list every Nth element.
# Sample list: [’a’, ’b’, ’c’, ’d’, ’e’, ’f’, ’g’, ’h’, ’i’, ’j’, ’k’, ’l’, ’m’, ’n’]
# Expected Output: [[’a’, ’d’, ’g’, ’j’, ’m’], [’b’, ’e’, ’h’, ’k’, ’n’], [’c’, ’f’, ’i’, ’l’]]

def split_list_every_nth(lst, n):
    split_lists = [lst[i::n] for i in range(n)]
    return split_lists

# Sample list
sample_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n = 3

# Split the list
result = split_list_every_nth(sample_list, n)
print(result)
