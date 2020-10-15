# Declare a beginning_and_end function that accepts a list of elements.
#
# It should return True if the first and last elements in the list are equal and False if they are unequal.
#
# Assume the list will always have at least 1 element.
#
# beginning_and_end([1, 2, 3, 1])     => True
# beginning_and_end([1, 2, 3, 4, 5])  => False
# beginning_and_end(["a", "b", "a"])  => True
# beginning_and_end([15])             => True

def beginning_and_end(lst):
	return lst[0] == lst[-1]

print(beginning_and_end([1, 2, 3, 1]))
print(beginning_and_end([1, 2, 3, 4, 5]))
print(beginning_and_end(["a", "b", "a"]))
print(beginning_and_end([15]))

print()

# Declare a long_word_in_collection function that accepts a list and a string. 
# The function should return True if 
#   - the string exists in the list AND
#   - the string has more than 4 characters.
#
# words = ["cat", "dog", "rhino"]
# long_word_in_collection(words, "rhino")  => True
# long_word_in_collection(words, "cat")    => False
# long_word_in_collection(words, "monkey") => False

def long_word_in_collection(lst, string):
	return string in lst and len(string) > 4

words = ["cat", "dog", "rhino"]
print(long_word_in_collection(words, "rhino"))
print(long_word_in_collection(words, "cat"))
print(long_word_in_collection(words, "monkey"))