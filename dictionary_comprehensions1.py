# example 1


# traditional method for creating dictionary from list where the dictionary's keys are the strings from the list and it's values are each element's length
def list_to_dict(lst):
	new_dict = {}
	for i in lst:
		new_dict[i] = len(i)
	return new_dict

programming_languages = ["Python", "Javascript", "Ruby"]
print(list_to_dict(programming_languages))
print()

# now using a dictionary comprehension
lengths = {i: len(i) for i in programming_languages}
print(lengths)
print()

# now using a dictionary comprehension to return a dictionary that has only letter 't' present in the key
only_t = {i: len(i) for i in programming_languages if 't' in i}
print(only_t)

# now returning a dictionary from a string where the key is the letter and the value is the number of times the letter occurs in the string

def str_to_dict(string):
	new_dict = {}
	for i in string:
		new_dict[i] = string.count(i)
	return new_dict

word = "supercalifragilisticexpialidocious"
print(str_to_dict(word))

# now using the above function in a dictionary comprehension
dict_comp = {i: word.count(i) for i in word}
print(dict_comp)