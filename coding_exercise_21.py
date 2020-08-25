# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
#
# EXAMPLES
# encrypt_message("abc") => "cde"
# encrypt_message("xyz") => "zab"
# encrypt_message("")    => ""

def encrypt_message(string):
	alphabet = "abcdefghijklmnopqrstuvwxyzab"
	new_string = ""
	try:
		for char in string:
			try:
				new_letter = alphabet.index(char) + 2
				new_string += alphabet[new_letter]
			except ValueError:
				print("substring not found")
	except TypeError:
			print("you can't iterate over an int or float!")
	return new_string

try:
	print(encrypt_message("abc"))
	print(encrypt_message("xyz"))
	print(encrypt_message(""))
except NameError:
	print("I don't see a name like that anywhere here!")