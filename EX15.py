# Write a Python program to shuffle and print a specified list.
"""n = input("Enter a items of list: ")
lst = list(map(int,n.split()))
print("-"*50)
print(lst)
print("-"*50)
print("Shuffled list = ",list(set(lst)) )"""

import random

n = input("Enter the items of the list: ")
lst = list(map(int, n.split()))

print("-" * 50)
print("Original list:", lst)

random.shuffle(lst)

print("-" * 50)
print("Shuffled list:", lst)
