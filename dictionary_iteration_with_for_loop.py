# example 1

chinese_food = {
	"Seasame Chicken": 9.99,
	"Boneless Spare Ribs": 7.99,
	"Fried Rice": 1.99,
}

# This solution for iteration is considered an Anti-Pattern: a solotion to a programming problem that is considered ineffective or counter-productive
for food in chinese_food:
	print(f"We have {food} and it's price is {chinese_food[food]}")
print()


# example 2
pounds_to_kilograms = {
	5: 2.26796,
	10: 4.53592,
	25: 11.3398,
}
for key in pounds_to_kilograms:
	print(f"{key} pounds is equal to {pounds_to_kilograms[key]}.")


print()
def lbs_to_kgs(int_num):
	formula = int_num / 2.205
	result = "{:.5f}".format(formula)
	return result
print(lbs_to_kgs(5))
print()


