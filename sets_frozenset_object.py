# a frozenset is a immutable set. any and all mutating methods for regular sets will NOT work with frozensets as frozensets are immutable 

mr_freeze = frozenset([1, 2, 3, 2])
print(mr_freeze)
print()
# a use case for frozenset.  a frozenset can serve as a dictionary key as it is immutable (only immutable data types can serve as dictionary keys)

print({mr_freeze: "some value"})
print()

my_dict = {
	mr_freeze: "another value"
}

print(my_dict)

# regular_set = {1, 2, 3}
# print({regular_set: "value"})
# this results in unhashable type error because the regular_set var is of mutable type

