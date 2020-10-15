random_numbers = [4, 8, 15, 16, 23, 42]

# building a list from a list that returns the square of each number element in a list
def return_square(num_list):
	squares = []
	for i in num_list:
		squares.append(i ** 2)
	return squares

print(return_square(random_numbers))
print()

# building a list from a list that returns floating point numbers from integers
def make_floats(num_list):
	floats = []
	for j in num_list:
		floats.append(float(j))
	return floats

print(make_floats(random_numbers))
print()


# building a list from a list that returns either True if the number element is even or False if the number element is odd
def even_or_odd_bool(num_list):
	bools = []
	for k in num_list:
		if k % 2 == 0:
			bools.append(True)
		else:
			bools.append(False)
	return bools

print(even_or_odd_bool(random_numbers))