# Write a Python program to print the numbers of a specified list after removing even numbers from it.
"""
lst = input("Enter numbers of list: ")
n = list(map(int, lst.split()))
for _ in n:
    print(_)
    print(len(n))
    print("-"*50)
    if(_%2==0):
        n.remove(_)
        print(len(n))
"""


lst = input("Enter numbers of the list: ")

n = list(map(int, lst.split()))
print("-"*50)
n = [s for s in n if s % 2 != 0]

print("List after removing even numbers:", n)
print("-"*50)
print(len(n))
