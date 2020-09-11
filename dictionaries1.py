# an unordered mutable data structure for declaring key value pairs
# a key is an object that serves as a unique identifier for a value
# a value is any object in Python

ice_cream_prefs = {"Ethan":"vanilla", "Stephanie":"strawberry", "Jason":"chocolate"}

for k,v in ice_cream_prefs.items():
	print(f"{k} likes {v}")