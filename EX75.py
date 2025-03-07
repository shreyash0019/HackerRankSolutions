# Write a Python program to extract a given number of randomly selected elements from a given list.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Selected 3 random numbers of the above list:
# [4, 4, 1]

import random
ol = [1, 1, 2, 3, 4, 4, 5, 1]
nl = []
for i in ol:
    e = random.choice(ol)
    nl.append(e)
    if len(nl) ==3:
        break

print(nl)

print("-"*25, "test-case-2", "-"*25)

al = [1, 1, 2, 3, 4, 4, 5, 1]
nl = random.choices(al, k=3)  # Picks 3 elements with replacement

print(nl)
