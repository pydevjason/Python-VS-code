# the filter function extracts a subset of values from a list based on a condition being met.  The filter function accepts two arguments like the map function, an function and an iterable.  The difference is the function we pass into filter must return a boolean value.  The boolean will determine whether the element in the iterable will be kept or discarded 

reptiles = ["snake", "lizard", "dragon", "dinosaur", "gecko", "skink"]

# return a new list with all elements that have a length greater than five elements

def more_reptiles(str_list):
	return len(str_list) > 5

print(list(filter(more_reptiles, reptiles)))
print()

def more_reptiles2(str_list):
	return [i for i in str_list if len(i) > 5]

print(more_reptiles2(reptiles))