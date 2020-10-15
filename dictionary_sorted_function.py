# reviewing using sorted() with lists

numbers = [4, 7, 2, 9]
print(sorted(numbers))

# if you pass a dictionary to the sorted() function it will return a list with the keys

salaries = {
	"Executive Assistant": 20,
	"CEO": 100,
}

print(sorted(salaries))

# sorted() can be used for iterating over a dictionary and return the objects in ascending order.

wheel_count = {
	"truck": 2,
	"car": 4,
	"bus": 8,
}

for vehicle, count in sorted(wheel_count.items()):
	print(f"The next vehicle is a {vehicle} and it has {count} wheels.")