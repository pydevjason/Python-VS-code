# list comprehension to create a list from a string
# find a given strings index position relative to the alphabet



def string_index_position(string):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	return [alphabet.index(i) for i in string]

print(string_index_position("steak"))
print()

# return a list of numbers within a range divided by 2

def divide_range():
	return [i / 2 for i in range(21)]

print(divide_range())
print()

flavors = [
"chocolate cream",
"vanilla",
"sweet cream",
"blueberry",
"cheesecake cream"]

# return a new string with only the elements with 'cream' in them.  Use both traditional and list comprehension methods
def creamy(lst):
	new_list = []
	for i in lst:
		if "cream" in i:
			new_list.append(i)
	return ", ".join(new_list)

print(creamy(flavors))
print()

def creamy2(lst):
	return [len(i) for i in lst if "cream" in i]

print(creamy2(flavors))
print()

# return a new list of elements from the elements that have 'cream' in them but return the new list without the word cream

def less_flavor(lst):
	new_list = []
	for i in lst:
		if "cream" in i:
			new_list.append(i.split(" ")[0])
	return new_list

print(less_flavor(flavors))
print()

def less_flavor2(lst):
	return [i.split(" ")[0] for i in lst if "cream" in i]

print(less_flavor2(flavors))