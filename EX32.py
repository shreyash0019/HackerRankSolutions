# Write a Python program to generate all sublists of a list.

def contains_sublist(main_list, sublist):
    # Loop through the main list
    for i in range(len(main_list) - len(sublist) + 1):
        # Check if the slice of the main list matches the sublist
        if main_list[i:i + len(sublist)] == sublist:
            return True
    return False


# Example usage
main_list = [1, 2, 3, 4, 5, 6]
sublist = [3, 4, 5]

if contains_sublist(main_list, sublist):
    print("The main list contains the sublist.")
else:
    print("The main list does not contain the sublist.")