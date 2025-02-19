# Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
# Sample list : [’p’, ’q’]
# n =5
# Sample Output : [’p1’, ’q1’, ’p2’, ’q2’, ’p3’, ’q3’, ’p4’, ’q4’, ’p5’, ’q5’]


n = int(input("Enter the number range (n): "))


lst2 = ['p', 'q']


result = [f"{item}{i}" for i in range(1, n + 1) for item in lst2]

print(result)

