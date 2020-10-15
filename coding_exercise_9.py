# Define a first_and_last function that accepts a list of strings. 
# The function should return a concatenation of the first element and the last element. 
# Assume the list will always have 1 or more elements.
#
# first_and_last(["x", "y", "z"])        => "xz"
# first_and_last(["eskimo", "excuses", "radon"])  => "eskimoradon"
# first_and_last(["i"])                  => "ii"

def first_and_last(str_list):
    return str_list[0] + str_list[-1]

print(first_and_last(["x", "y", "z"]))
print(first_and_last(["eskimo", "excuses", "radon"]))
print(first_and_last("i"))

print()

# Define a product_of_even_indices function that accepts a list of numbers. 
# The list will always have 6 total elements. 
# The function should return the product (multiplied total) of all numbers at an even index (0, 2, 4).
#
# product_of_even_indices([3, 6, 9, 12, 15, 18])    =>  405
# product_of_even_indices([2, 4, 6, 8, 10, 12])    =>  120

def product_of_even_indices(num_list):
    return num_list[0] * num_list[2] * num_list[4]

print(product_of_even_indices([3, 6, 9, 12, 15, 18]))
print(product_of_even_indices([2, 4, 6, 8, 10, 12]))

print()
# Define a first_letter_of_last_string function that accepts a list of strings. 
# It should return one character — the first letter of the last string in the list. 
# Assume the list will always have at least one string.
#
# first_letter_of_last_string(["wombat", "honey badger", "urchin"]) => "u"
# first_letter_of_last_string(["retrograde"]) => "r"

def first_letter_of_last_string(str_list):
    return str_list[-1][0]

print(first_letter_of_last_string(["wombat", "honey badger", "urchin"]))
print(first_letter_of_last_string(["retrograde"]))