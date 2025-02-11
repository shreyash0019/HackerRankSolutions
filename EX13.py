# Write a Python program to generate a 3*4*6 3D array whose each element is *.

"""import numpy as np

# Create a 3x4x6 array filled with '*'
array = np.full((3, 4, 6), '*', dtype=str)

# Print the array
print(array)
"""

# Create a 3D array using list comprehensions
array = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]

# Print the 3D array
for layer in array:
    print(layer)  # Each layer is a 2D array
