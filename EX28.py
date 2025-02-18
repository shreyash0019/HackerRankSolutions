# Write a Python program to get unique values from a list.

n = input("Enter the values of list: ").split()
lst = list(n)
print("-"*50)
print("unique values list")
unique_values = []

# Check for uniqueness
for i in lst:
    if i not in unique_values:
        unique_values.append(i)

print(unique_values)