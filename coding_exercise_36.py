# Assign a list of four dictionaries to a "complexity" variable below

# The first and third dictionaries should have two key-value pairs
# For those dictionaries, the keys should be strings and the values should be Booleans

# The second and fourth dictionaries should have three key-value pairs
# For those dictionaries, the keys shoulds be floats and the values should be list of strings. 
# The lists can be of any length.

complexity = [
	{
		"a": True,
		"b": False,
	},
	{
		1.1: ["str1", "str2", "str3"],
		2.2: ["str4", "str5", "str6"],
		3.3: ["str7", "str8", "str9"],
	},
	{
		"c": True,
		"d": False,
	},
	{
		4.4: ["str10", "str11", "str12"],
		5.5: ["str13", "str14", "str15"],
		6.6: ["str16", "str17", "str18"],
	},
]

print(complexity)