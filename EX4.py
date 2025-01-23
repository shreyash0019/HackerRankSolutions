# Write a Python program to get the smallest number from a list.

n = input("Enter a elements of list separated by space: ")
lst = list(map(int, n.split()))
lst.sort()
smallest_number = lst[0]
print(f"{smallest_number} is the smallest number of list")