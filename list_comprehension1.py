# list comp way
numbers = [3, 4, 5, 6, 7]

def get_square(num_list):
	return [pow(i, 2) for i in num_list]

print(get_square(numbers))

print()
# traditional way using for loop
def get_square2(num_list):
	squares = []
	for j in num_list:
		squares.append(pow(j, 2))
	return squares

print(get_square2(numbers))

print()
# list comp example 2:
# generate a new list with the lengths of each element
programming_language = ["Java", "Python", "Javascript", "Typescript"]

def str_length(str_list):
	return [len(k) for k in str_list]

print(str_length(programming_language))
print()

# return all elements in a new list lowercase
canon_dslr = ["EOS 1D", "EOS 5D", "EOS 6D", "EOS 7D"]

def lower_case(str_list):
	return [j.lower() for j in str_list]

print(lower_case(canon_dslr))
print()

# return all floating point values to integers in a new list

floats = [23.3, 1.45, 78.78, 12.2]

def convert_to_int(float_list):
	return [int(i) for i in float_list]

print(convert_to_int(floats))

