# Write a Python program to sum all the items in a list.

n = input("Enter Numbers in list: ")
lst = list(map(int, n.split()))
c = 0
for i in lst:
    c+=i
print("the sum of all numbers in list is {}".format(c))

