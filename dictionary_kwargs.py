# example 1

def collect_keyword_args(**kwargs):
	print(kwargs)
	print()
	for key, value in kwargs.items():
		print(f"The key is {key} and the value is {value}")

collect_keyword_args(a = 2, b = 4, c = 6)

print()
# now combining both *args and **kwargs into a function.  The *agrs param must always come before the **kwargs param.  In this example we will sum a and b, *args, and then *kwargs

def args_and_kwargs(a, b, *args, **kwargs):
	print(f"The sum of the regular arguments is {a + b}")
	print(f"The sum of the *args tuple is {sum(args)}")
	print(f"The sum of the **kwargs dictionary is {sum(kwargs.values())}")

	# another way of summing kwargs is:
	total = 0
	for i in kwargs.values():
		total += i
	print(f"The total of the values in kwargs is {total}")
	print()
	print(f"The total for kwargs using a list comprehension is {sum([i for i in kwargs.values()])}")

args_and_kwargs(1, 2, 3, 4, 5, 6, x = 8, y = 9, z = 10)
