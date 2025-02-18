# Write a Python program to count the number of elements in a list within a specified range.

# Input the range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# List of elements
lst = [1, 2, 3, 4, 5, 6, 7]

# Count elements within the specified range
count = 0
for i in lst:
    if start <= i <= end:
        count += 1

print(f"Number of elements in the range [{start}, {end}]: {count}")
