# Write a Python program to remove duplicates from a list.

lst = input("Enter the elements of list")
n = list(map(int, lst.split()))
print(n)
print("-"*50)
lst_without_duplicate = set(n)
print(list(lst_without_duplicate))


"""lst = input("Enter the elements of list: ")
n = list(map(int, lst.split()))
print(n)
print("-" * 50)

# Remove duplicates while maintaining order
lst_without_duplicates = []
for i in n:
    if i not in lst_without_duplicates:
        lst_without_duplicates.append(i)

print(lst_without_duplicates)
"""