# Write a Python program access the index of a list.
lst = [10,50,40,8]
i = 0
for x in lst:
    i+=1
    print(i, "->", x)

print("-"*50)

# Example list
lst = ['a', 'b', 'c', 'd', 'e']

# Using enumerate to get the index and element
for index, value in enumerate(lst):
    print(f"Index: {index}, Value: {value}")
