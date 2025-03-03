# Write a Python program to find the list in a list of lists whose sum of elements is the highest.
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]
Sample_lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
max_sum = 0
max_list = []

for i in Sample_lists:
    current_sum = 0
    for j in i:
        current_sum += j
    if current_sum > max_sum:
        max_sum = current_sum
        max_list = i

print("The list with the highest sum of elements is:")
print(max_list)

