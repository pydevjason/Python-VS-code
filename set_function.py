# the only way we can have an empty set in Python is to use the set() function since Python will interpret {} as an empty dictionary

print(set([1, 2, 3]))
print(set([1, 2, 3, 3, 2, 1]))
print(set((1, 2)))
print(set((1, 2, 2, 1, 2, 1)))
print(set("abc"))
print(set({"key": "value"}))
print()

# how to de-duplicate values from a list using set() function
philosophers = ["Plato", "Aristotle", "Socrates", "Pythagoras", "Socrates", "Plato"]
philosophers_set = set(philosophers)
philosophers = list(philosophers_set)
print(philosophers)