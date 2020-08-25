# Define an only_evens function that accepts a list of numbers. 
# It should return a new list consisting of only the even numbers from the original list.
#
# EXAMPLES
# only_evens([4, 8, 15, 16, 23, 42]) => [4, 8, 16, 42]
# only_evens([1, 3, 5])              => []
# only_evens([])                     => []

def only_evens(num_list):
	evens = []
	for i in num_list:
		if i % 2 == 0:
			evens.append(i)
	return evens

print(only_evens([4, 8, 15, 16, 23, 42]))
print(only_evens([1, 3, 5]))
print(only_evens([]))

print()
# Define a long_strings function that accepts a list of strings. 
# It should return a new list consisting of only the strings that have 5 characters or more.
#
# EXAMPLES
# long_strings(["Hello", "Goodbye", "Sam"])  => ["Hello", "Goodbye"]
# long_strings(["Ace", "Cat", "Job"])        => []
# long_strings([])                           => []

def long_strings(str_list):
	new_list = []
	for j in str_list:
		if len(j) >= 5:
			new_list.append(j)
	return new_list

print(long_strings(["Hello", "Goodbye", "Sam"]))
print(long_strings(["Ace", "Cat", "Job"]))
print(long_strings([]))
