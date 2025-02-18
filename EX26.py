# Write a Python program to find the second smallest number in a list.
def smallest_n():
    lst = [50, 20, 40, 55, 89, 90, 90, 1, 1]
    print(lst)
    print("-"*50)
    a = set(lst)
    print(a)
    print("-"*50)
    b = list(a)
    print(b)
    print("-" * 50)
    b.sort()

    smalln = b[1]
    print("{} is the smallest value in list".format(smalln))

#main program

smallest_n()
