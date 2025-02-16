# Write a Python program to find the index of an item in a specified list.
n = input("Enter the numbers of list: ")
lst = list(n.split())
print("-"*50)
print(n)
print("-"*50)
a = input("Enter a item of list u want to find its index: ")
print("-"*50)
c = lst.index(a)
if a in n:
    print("this item is present at {}".format(c))

else:
    print("{} Not present in list".format(a))
