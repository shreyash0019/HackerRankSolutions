#  Write a Python program to concatenate elements of a list.

lst = ['a','b','c','d','e','f']
conc = []
for l in lst:
    l+=l
    conc.append(l)
print(conc)

print("-"*25, "method-2", "-"*25)

lst = ['a', 'b', 'c', 'd', 'e', 'f']
conca = ''.join(lst)
print(conca)
