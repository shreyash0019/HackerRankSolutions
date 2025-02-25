# Write a Python program to select the odd items of a list.

lst = [1,2,3,4,5,6,7,8,9,10]
ol = []
for l in lst:
    if l%2 != 0:
        ol.append(l)
print(ol)