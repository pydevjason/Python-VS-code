# both of these functions accept an iterable and return a boolean.  accepts any kind of truthy value and returns true but if only one falsy value returns false.  all() is looking for all the elements to be True.

print(all([True]))
print(all([True, True]))
print(all([True, True, False]))
print(all([2,4,6]))
print(all([0]))
print(all([""]))
print(all([1,3,7,0]))
print(all([])) # empty list evaluate to True
print(all(["a", "b"]))
print()
# The any() function returns True if any values are true.  Only one has to be true for it to evaluate to True

print(any([True]))
print(any([False, False]))
print(any([True, True, False]))
print(any([2,4,6]))
print(any([0]))
print(any([""]))
print(any([1,3,7,0]))
print(any([])) # empty list evaluate to True
print(any(["a", "b"]))