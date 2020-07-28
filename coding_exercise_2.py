# Define a same_first_and_last_letter function that accepts a string as an argument. 
# The function should return a True if the first and last character are equal, and False otherwise
# Assume the string will always have 1 or more characters.
#
# EXAMPLES:
# same_first_and_last_letter("runner")   => True
# same_first_and_last_letter("Runner")   => False
# same_first_and_last_letter("clock")    => False
# same_first_and_last_letter("q")        => True

def same_first_and_last_letter(string):
    return string[0] == string[-1]

print(same_first_and_last_letter("runner"))
print(same_first_and_last_letter("Runner"))
print(same_first_and_last_letter("clock"))
print(same_first_and_last_letter("q"))

print()

# Define a three_number_sum function that accepts a 3-character string as an argument. 
# The function should add up the sum of the digits of the string. 
# HINT: You’ll have to figure out a way to convert the string-ified numbers to integers.
#
# EXAMPLES:
# three_number_sum("123")   => 6
# three_number_sum("567")   => 18
# three_number_sum("444")   => 12
# three_number_sum("000")   => 0

# def three_number_sum(string):
#     sums = 0
#     for i in string:
#         sums += int(i)
#     return sums

# print(three_number_sum("123"))

def three_number_sum(number):
    return int(number[0]) + int(number[1] + int(number[2]))

print(three_number_sum("123"))

# type conversion for three_number_sum results in TypeErrror VS code
# I have the same solution as the solution instructor Boris shows, however, mine results in a TypeError..  need help