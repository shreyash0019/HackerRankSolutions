# 72. Write a Python program to flatten a given nested list structure.
# Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# Flatten list:
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

ol = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
op = []

for item in ol:
    if isinstance(item, list):
        for subitem in item:
            op.append(subitem)
    else:
        op.append(item)

print(op)

