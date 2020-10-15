data_science = ["NumPy", "Keras", "TensorFlow", "Matplotlib", "Pandas"]

# example 1 for reversing list using negative indexing
print(data_science[::-1])

print()

for j in data_science[::-1]:
	print(f"{j} has {len(j)} total characters")

print()
# example 2 using the reversed() function to reverse elements in list.
# the reversed() fn returns a special type of object called a generator object that can also be iterated over using the same syntax as a regular for loop.  In this method you are not getting back a list but rather a list_reverseiterator object instead.  Generators prove more effective when working with massive amounts of data as iteration occurs one sequence at a time rather than all at once.  This can dramatically reduce system resources needed to process the data and thus prove more effective

print(reversed(data_science))

print()

print(type(reversed(data_science)))

print()

for k in reversed(data_science):
	print(k)