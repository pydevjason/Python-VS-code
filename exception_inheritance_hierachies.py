class Mistake(Exception):
	pass

# StupidMistake and SillyMistake are called siblings because they both inherit from the same parent 

class StupidMistake(Mistake):
	pass

class SillyMistake(Mistake):
	pass

try:
	raise StupidMistake("Extra stupid mistake")
except StupidMistake as e:
	print(f"caught the error: {e}")

print()

try:
	raise StupidMistake("Extra stupid mistake")
except Mistake as e:
	print(f"caught the error: {e}")

print()

try:
	raise SillyMistake("Super silly mistake")
except Mistake as e:
	print(f"caught the error: {e}")