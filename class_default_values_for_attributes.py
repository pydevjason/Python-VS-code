class Book():
	def __init__(self, title, author, price = 14.99):
		self.title = title
		self.author = author
		self.price = price

# if consistency for an attribute is needed you can hard-code it in the __init__ method

# if a default value for price is declared in the __init__ parameter, then that value will be placed if no other is specified during instantiation.  

animal_farm = Book("Animal Farm", "George Orwell", price = 21.99)
gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald")
print(animal_farm.price)
print(gatsby.price)