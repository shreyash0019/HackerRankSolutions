# Write a Python program to remove consecutive duplicates of a given list.
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After removing consecutive duplicates:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

ol = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
el = []
for i in ol:
    if i not in el:
        el.append(i)
if i in el:
    el.append(i)
print(el)

print("-"*25,"test-case 2","-"*25)
ol = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
el = []

for i in range(len(ol)):
    if i == 0 or ol[i] != ol[i - 1]:
        el.append(ol[i])

print(el)
