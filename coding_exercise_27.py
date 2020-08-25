# Declare a greater_sum function that accepts two lists of numbers.
# It should return the list with the greatest sum.
# You can assume the lists will always have different sums.
#
# EXAMPLES
# greater_sum([1, 2, 3], [1, 2, 4]) => [1, 2, 4]
# greater_sum([4, 5], [2, 3, 6])    => [2, 3, 6]
# greater_sum([1], [])              => [1]

def greater_sum(num_list1, num_list2):
	for i in num_list1:
		if sum(num_list1) > sum(num_list2):
			return num_list1
		else:
			return num_list2

print(greater_sum([1, 2, 3], [1, 2, 4]))
print(greater_sum([4, 5], [2, 3, 6]))
print(greater_sum([1], []))
print()


# Declare a sum_difference function that accepts two lists of numbers.
# It should return the difference between the sum of values in the first list and the second list
#
# EXAMPLES
# sum_difference([1, 2, 3], [1, 2, 4]) => 6 - 7 => -1
# sum_difference([4, 5], [2, 3, 6])    => 9 - 11 => -2
# sum_difference([1], [])              => 1

def sum_difference(num_list1, num_list2):
	return sum(num_list1) - sum(num_list2)

print(sum_difference([1, 2, 3], [1, 2, 4]))
print(sum_difference([4, 5], [2, 3, 6]))
print(sum_difference([1], []))


