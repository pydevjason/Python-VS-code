# You are writing a Python program to model a remote control
# for a television set. Declare a stations_to_numbers
# function that accepts a dictionary. The keys will be
# channel numbers and the values will be the station names.
# For example...
channels = {
  2: "CBS",
  4: "NBC",
  5: "FOX",
  7: "ABC"
}
# The stations_to_numbers function should return an
# inverted dictionary where the keys are the station names
# and the values are the channel numbers
#
# stations_to_numbers(channels) => {'CBS': 2, 'NBC': 4, 'FOX': 5, 'ABC': 7}

def stations_to_numbers(dictionary):
	inverted_dict = {}
	for key, value in dictionary.items():
		if dictionary[key] == value:
			inverted_dict[value] = key
	return inverted_dict

print(stations_to_numbers(channels))
print()
# using dictionary comprehension here
dict_comp_1 = {v: k for k, v in channels.items()}
print(dict_comp_1)
print()


# Declare a coaster_conversion function that accepts a dictionary
# The keys of the dictionary will be strings representing roller coasters
# The values will be the heights of each coaster in meters
#
# Return a new dictionary with the same keys.
# The values should be the heights converted from meters to feet,
# The final values (in feet) should also be rounded to the closest integer
# HINT: 1 meter is equal to 3.28084 feet
# HINT: The round function rounds a number to the nearest integer
#
coasters = {
  "Kingda Ka": 139,
  "Top Thrill Dragster": 130,
  "Superman: Escape From Krypton": 126
}
#
# coaster_conversion(coasters) => {'Kingda Ka': 456, 'Top Thrill Dragster': 426, 'Superman: Escape From Krypton': 413}

def coaster_conversion(dictionary):
	new_conversion = {}
	for key, value in dictionary.items():
		new_conversion[key] = round(value * 3.28084)
	return new_conversion

print(coaster_conversion(coasters))
print()
# now using dictionary comprehension here
dict_comp_2 = {key: round(value * 3.28084) for key, value in coasters.items()}
print(dict_comp_2)
print()

my_dict = {
	"k1": 1,
	"k2": 2,
	"k3": 3,
}

new_dict = {}
for k, v in my_dict.items():
	new_dict[k] = v

print(new_dict)
print()

# Given the list below, write a dictionary comprehension to return a dictionary where the keys are the numbers and the values are their cubes. The dictionary should only use the numbers that are even.

numbers = [3, 6, 7, 12, 15]


int_dict_comp = {i: pow(i,3) for i in numbers if i % 2 == 0}
print(int_dict_comp)
	