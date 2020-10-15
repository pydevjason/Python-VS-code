def accept_stuff(*args):
	print(type(args))
	print(args)

accept_stuff(1)
print()
# returns greatest number in tuple
def max_num(*numbers):
	try:
		high_num = numbers[0]
		for i in numbers:
			if i > high_num:
				high_num = i
		return high_num
	except TypeError:
		print("can only accept numbers as arguments")

print(max_num(15,21,3))
print()

# unpacking arguments to functions using *
def product(a, b):
	return a * b

list_numbers = [2, 6]
tup_numbers = (2, 6)
print(product(*list_numbers))


