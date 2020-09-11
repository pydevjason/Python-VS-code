# Declare a common_elements function that accepts a dictionary
# It should return a list with all of the elements that are found
# as both a key and a value in the dictionary
#
# HINT: Use the in operation to check for inclusion in a view or list object
#
# EXAMPLE:
my_dict = {
  "A": "K",
  "B": "D",
  "C": "A",
  "D": "Z"
}
#
# common_elements(my_dict) => ["A", "D"]

def common_elements(dictionary):
	new_list = []
	for key in dictionary.keys():
		if key in dictionary.values():
			new_list.append(key)
	return new_list
print(common_elements(my_dict))

