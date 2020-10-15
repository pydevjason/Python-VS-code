# exception handling is simply placing code to handle errors when the program doesn't execute the way it was designed to.  In this way the program won't crash if the error is "caught" and another approach is "tried"

# example 1

def divide_five_by_num(num):
	try:
		return 5 / num
	except ZeroDivisionError:
		return "you cannot divide by zero, try again"
	except TypeError as err:
		return f"you can only input ints and floats, not strings {err}"

try:
	print(divide_five_by_num("sldkc"))
except NameError:
	print("that input is invalid, try again!")
except TypeError:
	print("You did not pass a required argument to the function!")
