# Write a Python program to find the list of words that are longer than n from a given list of words.

words = input("Enter a list of words separated by spaces: ").split()
n = int(input("Enter the length threshold (n): "))

long_words = [word for word in words if len(word) > n]
ad = len(long_words)
print(f"Words longer than {n} characters: {long_words}")
print("words longer than {} are : {}".format(n,ad))

# apple banana cat elephant dog grape orange : inputs