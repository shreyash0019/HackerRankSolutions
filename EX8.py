# Write a Python program to check a list is empty or not.
n = input("Enter the elements of list: ")
lst = list(map(int, n.split()))
if len(lst)>0:
    print("List is not empty")
else:
    print("list is empty")