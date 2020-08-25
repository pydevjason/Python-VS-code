# accepts two arguments, the first is a function, and the second is an iterable such as a list or string.

numbers = [4, 8, 15, 16, 23, 42]
cubed = [pow(i, 3) for i in numbers]
print(cubed)

print()

def cube(number):
	return pow(number, 3)

print(list(map(cube, numbers)))
print()

# using map()
animals = ["dog", "cat", "ferret", "rat", "fish", "honey badger"]

def types_of_animals(str_list):
	return len(str_list)

print(list(map(types_of_animals, animals)))
print()

# using traditional for loop
def types_of_animals2(str_list):
	list_length = []
	for i in str_list:
		list_length.append(len(i))
	return list_length

print(types_of_animals2(animals))
print()

# using list comprehension
def types_of_animals3(str_list):
	return [len(i) for i in str_list]

print(list(map(types_of_animals3, animals)))