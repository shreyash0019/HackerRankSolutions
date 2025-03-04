# 70. Write a Python program to find the items starts with specific character from a given list.
# Expected Output:
# Original list:
# [’abcd’, ’abc’, ’bcd’, ’bkie’, ’cder’, ’cdsw’, ’sdfsd’, ’dagfa’, ’acjd’]
# Items start with a from the said list:
# [’abcd’, ’abc’, ’acjd’]
# Items start with d from the said list:
# [’dagfa’]
# Items start with w from the said list:
# []

ol = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
res = [], [], [], []
for i in ol:
    if i.startswith("a"):
        res[0].append(i)
    if i.startswith("b"):
        res[1].append(i)
    if i.startswith("c"):
        res[2].append(i)
    if i.startswith("d"):
        res[3].append(i)

print("list start with a : {}".format(res[0]))
print("list start with b : {}".format(res[1]))
print("list start with c : {}".format(res[2]))
print("list start with d : {}".format(res[3]))

print("-"*25, "test-case-2", "-"*25)

ol = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
char_to_find = ['a', 'b', 'c', 'd']
res = {char: [] for char in char_to_find}

for item in ol:
    for char in res:
        if item.startswith(char):
            res[char].append(item)

print("Original list: \n{}".format(ol))


for char in res:
    print(f"Items start with '{char}' from the said list:")
    print(res[char])
