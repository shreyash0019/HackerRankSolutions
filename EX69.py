# Write a Python program to check whether all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False
def ison():


    sample_list = [{}, {}, {}]
    for i in sample_list:
        if not i:
            return "True"
        else:
            return "False"


ison()

