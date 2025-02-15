# Write a Python program to convert a list of characters into a string.

n = list(input("Enter elements of list: "))
print("-"*50)
print(type(n))
print("-"*50)
s = "".join(n)
print(s, type(s))