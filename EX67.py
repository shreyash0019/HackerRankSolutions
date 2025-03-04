# Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]
# Sample list
sm_ls = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]


ls = []

# Loop through the sample list
for i in sm_ls:
    if i not in ls:
        ls.append(i)

print("New List:")
print(ls)
