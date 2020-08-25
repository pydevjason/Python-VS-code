# Define a word_lengths function that accepts a string. 
# It should return a list with the lengths of each word.
#
# EXAMPLES
# word_lengths("Mary Poppins was a nanny")  
# => [4, 7, 3, 1, 5]

# word_lengths("Somebody stole my donut")   
# => [8, 5, 2, 5]

def word_lengths(string):
	string = string.split(" ")
	list_lengths = []
	for i in string:
		list_lengths.append(len(i))
	return list_lengths

print(word_lengths("Mary Poppins was a nanny"))
print(word_lengths("Somebody stole my donut"))


# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string
#
# cleanup(["cat", "er", "pillar"])           
# => "cat er pillar"

# cleanup(["cat", " ", "er", "", "pillar"])  
# => "cat er pillar"

# cleanup(["", "", " "])                     => ""

def cleanup(str_list):
	new_string = []
	for i in str_list:
		if i.isspace() or len(i) == 0:
			continue
		else:
			new_string.append(i)
	return " ".join(new_string)

print(cleanup(["cat", "er", "pillar"]))
print(cleanup(["cat", " ", "er", "", "pillar"]))
print(cleanup(["", "", " "]))