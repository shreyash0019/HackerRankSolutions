# Write a python program to check whether two lists are circularly identical.

l1 = input("Enter list 1: ").split()
l2 = input("Enter list 2: ").split()

if len(l1) == len(l2) and len(l1) > 0 and ' '.join(l2) in ' '.join(l1 + l1):
    print("Both lists are circularly identical")
else:
    print("Both lists are different")
