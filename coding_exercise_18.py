# Write a factors function that accepts a positive whole number
# It should return a list of all of the number's factors in ascending order.
#
# EXAMPLES
# factors(1)  => [1]
# factors(2)  => [1, 2]
# factors(10) => [1, 2, 5, 10]
# factors(64) => [1, 2, 4, 8, 16, 32, 64]

def factors(pos_num):
	factors_list = []
	for i in range(1, pos_num + 1):
		if pos_num % i == 0:
			factors_list.append(i)
	return factors_list

print(factors(64))
