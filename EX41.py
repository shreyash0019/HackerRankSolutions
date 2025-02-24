# Write a Python program to split a list into different variables.

# Original list
lst = ["abc", 35.56, 100]

# Split the list into different variables
var1, var2, var3 = lst

# Print the variables
print("Variable 1:", var1)
print("Variable 2:", var2)
print("Variable 3:", var3)

print("-"*50)
# Approach 2

# Original list
lst = ["abc", 35.56, 100]

# Split the list into different variables using indexing
var1 = lst[0]
var2 = lst[1]
var3 = lst[2]

# Print the variables
print("Variable 1:", var1)
print("Variable 2:", var2)
print("Variable 3:", var3)

print("-"*50)
# Approach 3

# Original list
lst = ["abc", 35.56, 100]

# Split the list into different variables using a loop
variables = {}
for i in range(len(lst)):
    variables[f'var{i+1}'] = lst[i]

# Print the variables
for key, value in variables.items():
    print(f"{key}: {value}")

print("-" * 50)
