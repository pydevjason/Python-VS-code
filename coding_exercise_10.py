# Define a split_in_two function that accepts a list and a number.
# If the number is even, return the list elements from the third element to the end of the list.
# If the number is odd, return the list elements from index 0 (inclusive) to 2 (exclusive)
#
# EXAMPLE:
# values = ["a", "b", "c", "d", "e", "f"]
# split_in_two(values, 3)     => ["a", "b"]
# split_in_two(values, 4)     => ["c", "d", "e", "f"]
# split_in_two(values, 1)     => ["a", "b"]
# split_in_two(values, 10)    => ["c", "d", "e", "f"]

def split_in_two(lst, number):
	if number % 2 == 0:
		return lst[2:]
	elif number % 2 == 1:
		return lst[0:2]

values = ["a", "b", "c", "d", "e", "f"]
print(split_in_two(values, 10))


# Declare a nested_extraction function that accepts a list of lists and an index position.
#
# The function should use the index as the basis of finding both the nested list 
# and the element from that list with the given index position
#
# You can assume the number of lists will always be equal to 
# the number of elements within each of them.
#
# nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
# nested_extraction(nl, 0)  => 3
# nested_extraction(nl, 1)  => 8
# nested_extraction(nl, 2)  => 12

def nested_extraction(nested_list, idx):
	return nested_list[idx][idx]

nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
print(nested_extraction(nl, 0))
print(nested_extraction(nl, 1))
print(nested_extraction(nl, 2))


