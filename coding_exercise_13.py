# Define a smallest_number function  that accepts a list of numbers.
# It should return the smallest value in the list.
#
# smallest_number([1, 2, 3])     => 1
# smallest_number([3, 2, 1])     => 1
# smallest_number([4, 5, 4])     => 4
# smallest_number([-3, -2, -1])  => -3

def smallest_number(num_list):
	lowest_num = num_list[0]
	for i in num_list:
		if i < lowest_num:
			lowest_num = i
	return lowest_num

print(smallest_number([1, 2, 3]))
print(smallest_number([3, 2, 1]))
print(smallest_number([4, 5, 4]))
print(smallest_number([-3, -2, -1]))

print()
# Define a concatenate function that accepts a list of strings. 
#
# The function should return a concatenated string which consists of
# all list elements whose length is greater than 2 characters.
#
# concatenate(["abc", "def", "ghi"])      => "abcdefghi"
# concatenate(["abc", "de", "fgh", "ic"]) => "abcfgh"
# concatenate(["ab", "cd", "ef", "gh"])   => ""

def concatenate(str_list):
	new_string = ""
	for i in str_list:
		if len(i) > 2:
			new_string += i
	return new_string

print(concatenate(["abc", "def", "ghi"]))
print(concatenate(["abc", "de", "fgh", "ic"]))


print()
# Define a super_sum function that accepts a list of strings. 
# The function should sum the index positions of the first occurence of the letter “s” in each word. 
#
# Not every word is guaranteed to have an “s”.
# Don’t use "sum" as a variable name as it’s a built-in keyword.
#
# super_sum([])                                 => 0
# super_sum(["mustache"])                       => 2
# super_sum(["mustache", "greatest"])           => 8
# super_sum(["mustache", "pessimist"])          => 4
# super_sum(["mustache", "greatest", "almost"]) => 12

def super_sum(str_list):
	s_total = 0
	for i in str_list:
		if "s" in i:
			s_total += i.index("s")
	return s_total

print(super_sum([]))
print(super_sum(["mustache"]))
print(super_sum(["mustache", "greatest"]))
print(super_sum(["mustache", "pessimist"]))
print(super_sum(["mustache", "greatest", "almost"]))