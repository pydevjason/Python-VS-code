# Define a sum_of_lengths function that accepts a list of strings.
# The function should return the sum of the string lengths.
#
# EXAMPLES
# sum_of_lengths(["Hello", "Bob"])                  => 8
# sum_of_lengths(["Nonsense"])                      => 8
# sum_of_lengths(["Nonsense", "or", "confidence"])  => 20

def sum_of_lengths(str_list):
	total = 0
	for i in str_list:
		total += len(i)
	return total

print(sum_of_lengths(["Hello", "Bob"]))
print(sum_of_lengths(["Nonsense"]))
print(sum_of_lengths(["Nonsense", "or", "confidence"]))

print()

# Define a product function that accepts a list of numbers.
# The function should return the product of the numbers.
# The list will always have at least one value.
# product([1, 2, 3])     => 6
# product([4, 5, 6, 7])  => 840
# product([10])          => 10

def product(num_list):
	multiplier = 1
	for i in num_list:
		multiplier *= i
	return multiplier

print(product([1, 2, 3]))
print(product([4, 5, 6, 7]))
print(product([10]))