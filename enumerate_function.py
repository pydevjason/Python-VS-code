# using the enumerate() function we can track an elements index position or keep track of elements in numeric order.

storage_types = ["secure digital", "compact flash", "SSD", "HDD",]
print(enumerate(storage_types))

print()

# the enumerate() will return a generator object which is similar to a list.  You can also pass a second parameter to it, an int, for which you want it's default numeric starting position
print("Several types of storage media are:\n")
for i,v in enumerate(storage_types, 1):
	print(f"{i}. {v}")