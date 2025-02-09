# Write a Python program to clone or copy a list.
n = input("Enter elements of list: ")
lst = list(map(int, n.split()))
print(lst,id(lst))
print("-"*50)
lst1 = lst
print(lst1,id(lst1))
print("-"*50)
lst2 =lst.copy()
print(lst2,id(lst2))