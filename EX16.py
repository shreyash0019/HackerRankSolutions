# Write a Python program to generate and print a list except for the first 5 elements, where the values
# are square of numbers between 1 and 30 (both included).


squares = [x ** 2 for x in range(1, 31)]


result = squares[5:]


print("List of squares from 6:", result)
print("-"*150)
squares = [x ** 2 for x in range(1, 31)]


result = squares[5:25]


print("List of squares from 6:", result)

