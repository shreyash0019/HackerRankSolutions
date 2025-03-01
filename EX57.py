# Write a Python program to check whether the n-th element exists in a given list.

l = range(1,16)
lst = list(l)
n = int(input("Enter a number you want to find in list: "))
for i in lst:
    if i == n:
        print("element exists")
        break
    else:
        print("element doesnt exists")

print("-"*25, "test-case 2", "-"*25)

# Create the list
lst = list(range(1, 16))

# Get the index from user input
n = int(input("Enter the index you want to check: "))

# Check if the n-th element exists
if 0 <= n < len(lst):
    print(f"The {n}-th element exists and is: {lst[n]}")
else:
    print(f"The {n}-th element does not exist in the list.")
