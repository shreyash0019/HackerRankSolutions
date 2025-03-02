#  Write a Python program to iterate over two lists simultaneously.

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

for i, j in zip(l1, l2):
    print(i, j)

