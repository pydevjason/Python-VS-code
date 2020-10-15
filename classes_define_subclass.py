class Store():
	def __init__(self):
		self.owner = "Jason"

	def exclaim(self):
		return "Lots of coffee to taste, come inside!"

class CoffeeShop(Store):
	pass

my_coffee_shop = CoffeeShop()
print(my_coffee_shop.owner)
print(my_coffee_shop.exclaim())
print("\n")

# Declare a HardwareStore subclass that inherits from the Store superclass.
# Do not define any attributes and methods on the subclass. 
# Use the pass keyword to avoid a class body in HardwareStore.
# Instantiate a new instance of the HardwareStore class and assign it to a home_depot variable.
# Access the value of the "owner" attribute on your HardwareStore instance.
# Invoke the exclaim instance method on your HardwareStore instance.

class Store():
    def __init__(self):
        self.owner = "Boris"
  
    def exclaim(self):
        return "I'm defined in the superclass!"


class HardwareStore(Store):
	pass

home_depot = HardwareStore()
print(home_depot.owner)
print(home_depot.exclaim())



















