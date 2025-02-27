# Write a Python program to create a list with infinite elements.

def infinite_list_generator():
    num = 0
    while True:
        yield num
        num += 1

# Create an instance of the generator
infinite_gen = infinite_list_generator()

# Fetch the first 10 elements from the infinite generator
first_ten_elements = [next(infinite_gen) for _ in range(10)]
print(first_ten_elements)
