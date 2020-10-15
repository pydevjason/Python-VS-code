# to override a method means to define a different implementation of it on a subclass

class Teacher():
	def teach_class(self):
		print("teaching class...")

	def grab_lunch(self):
		print("getting lunch now...")

	def grade_tests(self):
		print("A+ A+ A+")

class CollegeProfessor(Teacher):
	def publish_book(self):
		print("Not only do I teach, I'm also an author!")

	# here is where the grade_tests method will be overridden by this other grade_tests method since it is newly defined in the CollegeProfessor class
	def grade_tests(self):
		print("B B B!")

teacher = Teacher()
professor = CollegeProfessor()

teacher.teach_class()
teacher.grab_lunch()
teacher.grade_tests()
print()
professor.teach_class()
professor.grab_lunch()
professor.publish_book()
professor.grade_tests()
print()

# Define a Clothing superclass with wear and sell instance methods.
# The wear method should return the string “I'm wearing this fashionable piece of clothing!”
# The sell method should return the string “Buy my piece of clothing!”

# Define a Socks subclass that inherits from the Clothing superclass.
# It should define a lose_one instance method that 
# returns the string “Where did my other one go?”
# It should override the wear method to 
# return the string “Take a look at my socks! They're gorgeous!”
# It should override the sell method to 
# return the string “Buy my socks!”

class Clothing():
	def wear(self):
		print("I'm wearing this fashionable piece of clothing!")

	def sell(self):
		print("Buy my piece of clothing!")

class Socks(Clothing):
	def lose_one(self):
		print("Where did my other one go?")

	def wear(self):
		print("Take a look at my socks! They're gorgeous!")

	def sell(self):
		print("Buy my socks!")

clothing = Clothing()
socks = Socks()

clothing.wear()
socks.wear()

































