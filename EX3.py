# Write a Python program to get the largest number from a list.
n = input("Enter a list to find its largest Number: ")
lst = list(map(int, n.split()))
lst.sort(reverse= True)
ans = lst[0]
print("Largest number of list is :{} ".format(ans))