# an instance method is a function that belongs to an object, all instance methods take a parameter of self

# class Pokemon():
# 	def __init__(self, name, specialty, health = 100):
# 		self.name = name
# 		self.specialty = specialty
# 		self.health = health

# 	def roar(self):
# 		print("Raaaar!!!")

# 	def describe(self):
# 		print(f"I am {self.name} and my specialty is {self.specialty}")

# 	def do_damage(self, amount):
# 		self.health -= amount

# squirtle = Pokemon("Squirtle", "Water")
# charmander = Pokemon("Charmander", "Fire", 150)

# charmander.describe()
# print()
# squirtle.do_damage(20)
# print(squirtle.health)
# print()


# Declare a Musician class that accepts age and income parameters. 

# In the instantiation process for an object, assign the two parameters
# to two attributes with the same name.

# Declare an enter_club instance method. 
# If the musician is less than 21 years old, the method should 
# return the string "Access denied!”. 
# If the musician is 21 or older, the method should
# return the string "Access granted!".

# Declare a play_show instance method. The method should
# increment the musician’s income by 5.

class Musician():
	def __init__(self, age, income):
		self.age = age
		self.income = income

	def enter_club(self):
		if self.age < 21:
			return "Access denied!"
		else:
			return "Access granted!"

	def play_show(self):
		self.income += 5

cliff = Musician(age = 27, income = 0)
print(cliff.age)    # 27
print(cliff.enter_club())  # "Access granted!"
print(cliff.income) # 0
cliff.play_show()
print(cliff.income) # 5
cliff.play_show()
print(cliff.income) # 10