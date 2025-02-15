# Write a Python program to generate all permutations of a list in Python.

from itertools import permutations

lst = [1, 2, 3]

# Convert permutations to a list of lists
perm_list = [list(p) for p in permutations(lst)]

print("-"*50)
print("List of lists for permutations:")
print("-"*50)

print(perm_list)



print("-"*50)

lst = [1, 2, 3]
print("Nested Loops Permutations:")
print("-"*50)

for i in lst:
    for j in lst:
        for k in lst:
            if i != j and j != k and i != k:
                print([i, j, k])


print("-"*50)


def generate_permutations(lst):
    # Base case: if the list has 1 element, return it as the only permutation
    if len(lst) == 1:
        return [lst]

    # Recursive case
    permutations = []
    for i in range(len(lst)):
        # Extract the current element
        current = lst[i]
        # Generate permutations for the remaining elements
        remaining = lst[:i] + lst[i + 1:]
        for p in generate_permutations(remaining):
            permutations.append([current] + p)
    return permutations


# Example usage
lst = [1, 2, 3]
result = generate_permutations(lst)
print("Permutations:", result)
print("-"*50)