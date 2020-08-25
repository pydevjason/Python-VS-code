breakfast = ["Eggs", "Cereal", "Banana"]
lunch = ["Sushi", "Chicken Teriyaki", "Soup"]
dinner = ["Steak", "Meatballs", "Pasta"]

print(zip(breakfast, lunch, dinner))
print()
print(list(zip(breakfast, lunch, dinner)))
print()

for x, y, z in zip(breakfast, lunch, dinner):
	print(f"My meals for today were {x} and {y} and {z}.")

print()

for a, b, c in zip([3, 2, 1], [1, 2, 3], [2, 3, 1]):
  print("*-*".join([str(a), str(b), str(c)]))

