# a list is a data structure that stores a mutable and ordered sequence of objects.  Also known as an array
# each object inside a list is called an element
# empty = list() this can be used if you want to convert another data structure/type to a list

empty = []

# the length of a list corresponds to how many elements are in the list
colors = ["red", "white", "blue"]
for i in colors:
    print(f"there are {len(i)} chars in {i}")
    
print()
# Declare an is_long function that accepts a single list as an argument
# It should return True if the list has more than 5 elements, and False otherwise

def is_long(lst):
    return len(lst) > 5

print(is_long([1,2,3,4,5,6]))
