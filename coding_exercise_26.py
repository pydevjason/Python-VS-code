# all solutions should use a combination of map, filter, and lambda

# Declare a right_words function that accepts a list of words and a number.
# Return a new list with the words that have a length equal to the number.
# Do NOT use list comprehension.
#
# EXAMPLES:
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3)     => ['cat', 'dog', 'ace']
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5)     => ['heart']
# right_words([], 4)                                         => []

# def right_words(word_list, number):
# 	new_list = []
# 	for i in word_list:
# 		if len(i) == number:
# 			new_list.append(i)
# 	return new_list

# print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3))
# print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5))
# print(right_words([], 4))

def right_words(word_list, number):
	return list(filter(lambda x: len(x) == number, word_list))

print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3))
print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5))
print(right_words([], 4))
print()

# Declare an only_odds function.
# It should accept a list of whole numbers.
# It should return a list with only the odd numbers from the original list.
# Do NOT use list comprehension.
#
# EXAMPLES:
# only_odds([1, 3, 5, 6, 7, 8])      =>  [1, 3, 5, 7]
# only_odds([2, 4, 6, 8])            =>  []

def only_odds(num_list):
	return list(filter(lambda x: x % 2 == 1, num_list))

print(only_odds([1, 3, 5, 6, 7, 8]))
print(only_odds([2, 4, 6, 8]))
print()

# Declare a count_of_a function that accepts a list of strings.
# It should return a list with counts of how many “a” characters appear per string.
# Do NOT use list comprehension.
#
# EXAMPLES:
# count_of_a(["alligator", "aardvark", "albatross"])    => [2, 3, 2]
# count_of_a(["plywood"])                               => [0]
# count_of_a([])                                        => []

def count_of_a(str_list):
	return list(map(lambda x: x.count("a"), str_list))

print(count_of_a(["alligator", "aardvark", "albatross"]))
print(count_of_a(["plywood"]))
print(count_of_a([]))
