# Write a Python program to get the frequency of the elements in a list.

n = input("Enter the elements of list: ")
lst = n.split()

# Create a dictionary to store frequencies
frequency = {}

# Count the frequency of each element
for i in lst:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print("-" * 50)
print("Frequency of elements:")
for key, value in frequency.items():
    print(f"{key}: {value}")
