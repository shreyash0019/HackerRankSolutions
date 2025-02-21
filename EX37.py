# Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350

sample_list = [11, 33, 50]


result = int("".join(map(str, sample_list)))

print("Expected Output:", result)

