# Write a Python program to pack consecutive duplicates of a given list elements into sublists.
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After packing consecutive duplicates of the said list elements into sublists:
# [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
def pack_sublists_value_change(main_list):
    sublists = []
    current_sublist = [main_list[0]]
    for item in main_list[1:]:
        if item != current_sublist[-1]:
            sublists.append(current_sublist)
            current_sublist = []
        current_sublist.append(item)
    sublists.append(current_sublist)
    return sublists


main_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
packed_list = pack_sublists_value_change(main_list)
print(packed_list)
