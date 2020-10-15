# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.
#
# EXAMPLES
# length_match(["cat", "dog", "kangaroo", "mouse"], 3))  => 2
# length_match(["cat", "dog", "kangaroo", "mouse"], 5))  => 1
# length_match(["cat", "dog", "kangaroo", "mouse"], 4))  => 0
# length_match([], 5))                                   => 0

def length_match(str_list, number):
	count = 0
	for i in str_list:
		if len(i) == number:
			count += 1
	return count

print(length_match(["cat", "dog", "kangaroo", "mouse"], 3))
print(length_match(["cat", "dog", "kangaroo", "mouse"], 5))
print(length_match(["cat", "dog", "kangaroo", "mouse"], 4))
print(length_match([], 5))

print()
# Declare a sum_from function that accepts two numbers as arguments.
# The second number will always be greater than the first number.
# The function should return the sum of all numbers from the first number to the second number (inclusive).
#
# EXAMPLES
# sum_from(1, 2)   # 1 + 2                  => 3
# sum_from(1, 5)   # 1 + 2 + 3 + 4 + 5      => 15
# sum_from(3, 8)   # 3 + 4 + 5 + 6 + 7 + 8  => 33
# sum_from(9, 12)  # 9 + 10 + 11 + 12       => 42

def sum_from(num1, num2):
	total = 0
	for j in range(num1, num2 + 1):
		total += j
	return total

print(sum_from(1, 2))
print(sum_from(1, 5))
print(sum_from(3, 8))
print(sum_from(9, 12))


print()
# Declare a same_index_values function that accepts two lists.
# The function should return a list of the index positions in which the two lists have equal elements
#
# EXAMPLES
# same_index_values([1, 2, 3], [3, 2, 1])                         => [1]
# same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"])   => [1, 3]

def same_index_values(list1, list2):
	new_list = []
	for i,v in enumerate(list1):
		if list1[i] == list2[i]:
			new_list.append(i)
	return new_list

print(same_index_values([1, 2, 3], [3, 2, 1]))
print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]))


# Your mission here is to create a function that accepts a tuple and returns a tuple with 3 elements - the first, third and second element from the last for the given array.

def easy_unpack(tup):
	a = elements[0]
	b = elements[2]
	c = elements[-2]
	return a,b,c

elements = (1, 2, 3, 4, 5, 6, 7, 9)
print(easy_unpack(elements))
print()


def return_first_word(string):
	return string.split()[0]

print(return_first_word("Hello World"))
print()


def is_acceptable_password(string):
	return len(string) > 6

print(is_acceptable_password("short"))
print(is_acceptable_password("muchlonger"))
print()



# make a function that accepts a string and returns the sum of only the numbers in the string.  
def sum_numbers(string):
	sums = 0
	numbers = []
	for letter in string.split():
		if letter.isdigit():
			numbers.append(int(letter))
	return sum(numbers)

print(sum_numbers('my 3 number is 2'))
print()

# You are given an array of integers. You should find the sum of the integers with even indexes (0th, 2nd, 4th...). Then multiply this summed number and the final element of the array together. Don't forget that the first element has an index of 0.

# For an empty array, the result will always be 0 (zero).

# Input: A list of integers.

# Output: The number as an integer.

def checkio(num_list):
	sums = 0
	for i in num_list[::2]:
		sums += i * num_list[-1]
	return sums

print(checkio([1,3,5]))
print(checkio([]))


# You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters. You should check if the string contains three words in succession. For example, the string "start 5 one two three 7 end" contains three words in succession.

# Input: A string with words.

# Output: The answer as a boolean.

def checkio2(string):
	string = string.split()
	for i in string:
		pass

print(checkio2("He is 123 man"))



