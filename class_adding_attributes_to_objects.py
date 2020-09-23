# class MacBookPro():
# 	def __init__(self):
# 		print(f"A MacBook Pro is being created.  This object is {self}")

# mac_book_pro_16 = MacBookPro()
# mac_book_pro_13 = MacBookPro()
# mac_book_pro_16.ssd = "512GB"
# mac_book_pro_16.graphics = "AMD Radeon 5500 4GB"
# mac_book_pro_16.ram = "16GB DDR4"
# mac_book_pro_16.year = 2020

# mac_book_pro_13 = "unavailable"

# print(mac_book_pro_16.year)

# to code this way in Python is possible however, writing this was is considered an anti-pattern because the two objects created cannot share the same attributes as they are supposed to in object oriented programming.  The goal of OOP is to have consistency across objects and their attributes.

class MacbookPro():
	def __init__(self, size, processor, storage, graphics, ram, year):
		self.size = size
		self.processor = processor
		self.storage = storage
		self.graphics = graphics
		self.ram = ram
		self.year = year

mac_book_pro_13 = MacBookPro("13 inch", "2.0GHz quad-core 10th-generation Intel Core i5 processor", "512GB SSD storage", "Intel Iris Plus Graphics", "16GB 3733MHz LPDDR4X memory", 2020)

mac_book_pro_16 = MacBookPro("16-inch Retina display with True Tone", "2.3GHz 8-core 9th-generation Intel Core i9 processor", "1TB of SSD storage", "AMD Radeon Pro 5500M with 4GB of GDDR6 memory", "16GB of 2666MHz DDR4 memory", 2020)