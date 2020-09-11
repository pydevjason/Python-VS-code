# Define a to_dictionary function that accepts a list of strings. 
# The function should return a dictionary where the keys are the strings 
# and the values are their original index positions in the list.
#
# EXAMPLE:
# detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
# to_dictionary(detectives) => {'Sherlock Holmes': 0, 'Hercule Poirot': 1, 'Nancy Drew': 2}

def to_dictionary(str_list):
	new_dict = {}
	for idx, element in enumerate(str_list):
		new_dict[element] = idx
	return new_dict

detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
print(to_dictionary(detectives))
print("\n")

# Define a length_counts function that accepts a list of strings. 
# The function should return a dictionary where the keys represent
# length and the values represent how many strings have that length.
#
# EXAMPLE:
# sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
# length_counts(sa_countries) => # {6: 1, 9: 2, 7: 2, 4: 1}
# There is 1 string with 6 letters, 2 strings with 9 letters, 
# 2 strings with 7 letters, and 1 string with 4 letters.

def length_counts(str_list):
	new_dict = {}
	for i in str_list:
		length = len(i)
		current_count = new_dict.get(length, 0)
		new_dict[length] = current_count + 1
	return new_dict

sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
print(length_counts(sa_countries))
