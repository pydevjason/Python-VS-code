# Declare a plenty_of_arguments function that accepts two parameters (a and b)
# and an additional **kwargs parameter.
#
# The function should return True if the sum of a, b, and the values of 
# **kwargs is greater than 100. It should return False otherwise.
#
# EXAMPLES:
# plenty_of_arguments(20, 30)                          => False
# plenty_of_arguments(a = 50, b = 75)                  => True
# plenty_of_arguments(a = 50, b = 25, c = 50)          => True
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 25)  => False
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 26)  => True

def plenty_of_arguments(a, b, **kwargs):
	first_two_args = a + b
	if first_two_args > 100:
		return True
	for i in kwargs.values():
		return first_two_args + sum(kwargs.values()) > 100
	return first_two_args > 100

print(plenty_of_arguments(20, 30))
print(plenty_of_arguments(a = 50, b = 75))
print(plenty_of_arguments(a = 50, b = 25, c = 50))
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 25))
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 26))
print()

# another example, this one much shorter and more pythonic

def plenty_of_arguments2(a, b, **kwargs):
	return a + b + sum(kwargs.values()) > 100

print(plenty_of_arguments2(20, 30))
print(plenty_of_arguments2(a = 50, b = 75))
print(plenty_of_arguments2(a = 50, b = 25, c = 50))
print(plenty_of_arguments2(a = 25, b = 25, c = 25, d = 25))
print(plenty_of_arguments2(a = 25, b = 25, c = 25, d = 26))
print()