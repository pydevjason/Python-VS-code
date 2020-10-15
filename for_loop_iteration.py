# an object is considered iterable if it's elements can be stepped through one by one

# example 1: iteration over a string

# fav_qoute = "preserve my life according to Your Word."

# printed with string length using a counter

# count = 1
# for k in fav_qoute:
# 	print(count, k)
# 	count += 1


# example 2: iteration over list

cell_types = [
			"Erythrocytes", 
			"Chondrocytes", 
			"Osteoclasts", 
			"Melanocytes",
]

for c in cell_types:
	print(len(c), c)

print()

numbers = [12, 24, 36, 48, 60, 72, 84]

for n in numbers:
	print(n * n)

print()

# simple program to add the int elements in a list
def add_list(lst):
	count = 0
	for i in lst:
		count += i
	return count

numbers = [12, 24, 36, 48, 60, 72, 84]
print(add_list(numbers))