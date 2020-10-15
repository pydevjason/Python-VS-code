class MacBookPro():
	def __init__(self, processor):
		self.processor = processor
		
mac_book_pro_16 = MacBookPro("2.6GHz 6-core 9th-generation Intel Core i7 processor")
mac_book_pro_13 = MacBookPro("2.0GHz quad-core 10th-generation Intel Core i5 processor")

print(mac_book_pro_16.processor)
print()


# Declare a Musical class that accepts a name parameter. 
# In the initialization process for an object, assign the
# name parameter to a name attribute on the object.
#
# Instantiate a Musical object with the name “Rent” 
# and assign it to an “rent" variable.
#
# Instantiate a second Musical object with the name “Book of Mormon" 
# and assign it to a “mormon” variable.
#
# Instantiate a third object from the class with the name “Chicago" 
# and assign it to a “chicago” variable.

class Musical():
	def __init__(self, name):
		self.name = name

rent = Musical("Rent")
mormon = Musical("Book of Mormon")
chicago = Musical("Chicago")



# Declare a Shape class that accepts a sides parameter. 

# In the initialization process for an object, assign the sides parameter to a sides attribute on the object.

# Instantiate a Shape object with 3 sides and assign it to a “triangle" variable.

# Instantiate a Shape object with 4 sides and assign it to a “square" variable.

# Instantiate a Shape object with 10 sides and assign it to a “decagon" variable.

class Shape():
	def __init__(self, sides):
		self.sides = sides

triangle = Shape(3)
square = Shape(4)
decagon = Shape(10)


# Declare a Skyscraper class that accepts name and year parameters. 

# In the initialization process for an object, assign the name parameter to a name attribute 
# and the year parameter to a year attribute.

# Instantiate a Skyscraper object with the name “Empire State Building”  and the year 1931. 
# Assign it to a “empire" variable.

# Instantiate a Skyscraper object with the name “One World Trade Center” and the year 2014. 
# Assign it to a “wtc" variable.


class Skyscraper():
	def __init__(self, name, year):
		self.name = name
		self.year = year

empire = Skyscraper("Empire State Building", 1931)
wtc = Skyscraper("One World Trade Center", 2014)





