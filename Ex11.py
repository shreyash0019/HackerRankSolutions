# Write a Python function that takes two lists and returns True if they have at least one common member.

def common():
    l1 = input("Enter list1 of words: ").split()
    l2 = input("Enter list2 of words: ").split()


    for word in l1:
        if word in l2:
            return True
    return False

#main program

if common():
    print("The lists have common words.")
else:
    print("The lists do not have common words.")