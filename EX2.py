# Write a Python program to multiply all the items in a list.

n = input("Enter the items of list: ")
lst = map(int, n.split())
i = 1
for ls in lst:
    i*= ls

print(i)