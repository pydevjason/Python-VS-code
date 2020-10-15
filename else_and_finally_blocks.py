# x = 10

try:
	print(x + 5)
except NameError:
	print("some variable is not defined")
else:
	print("this will print if there is no error in the try block")
finally:
	print("this will print with or without an exception")

print()

# class Problem(Exception):
#   pass
 
# class BusinessProblem(Problem):
#   pass
 
# class CodingProblem(Problem):
#   pass
 
# def monday_morning():
#   try:
#     raise Problem
#   except CodingProblem:
#     print("Will this print?")
 
# monday_morning() # no this will not print

# You got it! We are raising the superclass Problem exception, which will not be captured by the CodingProblem subclass.