# returns a shallow copy - only works when using a one dimensional list.  Does not work with nested data structures

length_units = ["meter", "centimeter", "inch", "foot", "millimeter", "kilometer", "yard", "mile", "decimeter", "astronomical unit"]
print(length_units)
print()

# these two are the same but they point to two different locations in memory.  They are two distinct objects
length_units_copy = length_units.copy()
print(id(length_units))
print(id(length_units_copy))
print()

print(length_units)
print(length_units_copy)
print()

# the shorthand syntax for a shallow copy is list[:]

