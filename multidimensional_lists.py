fizzy_water = [
			["lemon", "lime", "orange"],
			["cherry", "grape", "grapefruit"],
			["banana", "apple", "plain"]
]

print(len(fizzy_water))
print(fizzy_water)
print()

print(fizzy_water[0][1][0:3])
print(len(fizzy_water[1][1][0:2]))

def co2_drinks():
	lst = fizzy_water
	new_list = []
	for i in lst:
		for j in i:
			new_list.append(j)
	return new_list

print(co2_drinks())
print()


 
