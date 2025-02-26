# Write a Python program to convert list to list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{’color_name’: ’Black’, ’color_code’: ’#000000’}, {’color_name’: ’Red’, ’color_code’:
# ’#FF0000’}, {’color_name’: ’Maroon’, ’color_code’: ’#800000’}, {’color_name’: ’Yellow’, ’color_code’:
# ’#FFFF00’}]

def convert_to_dict_list(color_names, color_codes):
    return [{"color_name": name, "color_code": code} for name, code in zip(color_names, color_codes)]

# Sample lists
color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

# Convert lists to list of dictionaries
result = convert_to_dict_list(color_names, color_codes)

print(result)  # Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
