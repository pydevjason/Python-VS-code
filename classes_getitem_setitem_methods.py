# pillows = {
# 	"soft": 29.99,
# 	"firm": 49.99,
# }

# print(pillows["soft"])
# print(pillows.__getitem__("soft"))

# this class by itself is read-only, if we want to write to it we need to use the __setitem__ method inside the class

class CrayonBox():
	def __init__(self):
		self.crayons = []

	def add(self, crayon):
		self.crayons.append(crayon)

	def __getitem__(self, index):
		return self.crayons[index]

	def __setitem__(self, index, value):
		self.crayons[index] = value

cb = CrayonBox()
cb.add("Blue")
cb.add("Red")
print(cb[0])

cb[1] = "Yellow"
print(cb[1])

print()
print()
# the __getitem__ special method allows for the class to now use indexing to retrieve an attribute, without __getitem__ being inside the class trying to use indexing to retrieve an attribute would return an error


# Define a Car class that accepts a maker (string), model (string),
# and year (number) parameters and assigns them to respective
# attributes

# Define a Dealership class. Each Dealership object should instantiate
# with a "cars" attribute set to an empty list.

# A Dealership object should have a accept_delivery instance method
# that accepts a Car object and adds it to the Dealership's internal
# "cars" list

# Indexing into a Dealership with a number should access a specific
# Car object in the Dealership.

# An index position in a Dealership should also be overwriteable
# with a new Car object (see examples below)

class Car():
	def __init__(self, maker, model, year):
		self.maker = maker
		self.model = model
		self.year = year

class Dealership():
	def __init__(self):
		self.cars = []

	def accept_delivery(self, car):
		self.cars.append(car)

	def __getitem__(self, index):
		return self.cars[index]

	def __setitem__(self, index, value):
		self.cars[index] =  value


f150 = Car(maker = "Ford", model = "F-150", year = 2019)
camry = Car(maker = "Toyota", model = "Camry", year = 2020)
porsche = Car (maker = "Porsche", model = "911 Carrera", year = 2021)

dealership = Dealership()

dealership.accept_delivery(f150)
dealership.accept_delivery(camry)

print(dealership[0].year) # 2019 -- the F150's year

dealership[0] = porsche

for car in dealership:
  print(car.maker) # Porsche, Toyota
























