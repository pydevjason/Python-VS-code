# example 1
# creating a new dictionary from an existing dictionary

capitals = {
	"New York": "Albany",
	"California": "Sacramento",
	"Texas": "Austin",
}

# here we will create a new dictionary from the above dictionary where the keys and values are inverted.

def invert_dictionary(dictionary):
	new_dict = {}
	for key, value in dictionary.items():
		if dictionary[key] == value:
			new_dict[value] = key
	return new_dict

print(invert_dictionary(capitals))
print()

# now we will use the capitals dictionary as a dictionary comprehension with key:values inverted also returning key value pairs that are not equal in length

inv_dict = {v: k for k, v in capitals.items() if len(k) != len(v)}
print(inv_dict)
print()

values = [1, 2, 3, 4, 5]
print({ value: sum(values[:index + 2]) for index, value in enumerate(values) })