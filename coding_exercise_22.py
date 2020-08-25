# Define a word_lengths function that accepts a string. 
# It should return a list with the lengths of each word.
#
# EXAMPLES
# word_lengths("Mary Poppins was a nanny")  => [4, 7, 3, 1, 5]
# word_lengths("Somebody stole my donut")   => [8, 5, 2, 5]

def word_lengths(string):
	string = string.split(" ")
	item_length = []
	for i in string:
		item_length.append(len(i))
	return item_length
try:
	print(word_lengths("Mary Poppins was a nanny"))
	print(word_lengths("Somebody stole my donut"))
except NameError:
	print("The specifed name is not in the function")


	
