# Write a Python program to find the second largest number in a list.
def largest_n():
    lst = [5,8, 5, 8, 9, 7, 2, 2, 5 ,7]
    print(lst)
    print("-"*50)
    a = set(lst)
    print(a)
    print("-"*50)
    b = list(a)
    print(b)
    print("-" * 50)
    b.sort()

    largen = b[-2]
    print("{} is the second largest value in list".format(largen))

#main program

largest_n()