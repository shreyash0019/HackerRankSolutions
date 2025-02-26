# Write a Python program to compute the difference between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: [’white’, ’orange’, ’red’]
# Color2-Color1: [’black’, ’yellow’]

l1 = ["red", "orange", "green", "blue", "white"]
l2 = ["black", "yellow", "green", "blue"]
s1,s2 = set(l1),set(l2)
diff1 = s1-s2
diff2 = s2-s1
print(list(diff1))
print(list(diff2))