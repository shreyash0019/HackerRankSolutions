# 65. Write a Python program to move all zero digits to end of a given list of numbers.
# Expected output:
# Original list:
# [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# Move all zero digits to end of the said list of numbers:
# [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

sm_ls = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
ls =[]
for i in sm_ls:
    if i == 0:
        ls.append(i)
        sm_ls.remove(i)
print(ls)
print(sm_ls)
print("-"*50)
sm_ls.extend(ls)
print(sm_ls)

print("-"*25,"test-case:2", "-"*25)

# Original list
sm_ls = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

# List to hold non-zero elements
non_zero_ls = [i for i in sm_ls if i != 0]

# List to hold zero elements
zero_ls = [i for i in sm_ls if i == 0]

# Combine the lists
result_ls = non_zero_ls + zero_ls

print("Original list:")
print(sm_ls)
print("Move all zero digits to end of the said list of numbers:")
print(result_ls)
