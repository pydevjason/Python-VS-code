# Have the function FindIntersection(strArr) read the  array of strings stored in strArr which will contain 2 elements: 

# the first element will represent a list of comma-separated numbers sorted in ascending order, 

# the second element will represent a second list of comma-separated numbers (also sorted). 

# Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.

# Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
# Output: 1,4,13

# Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
# Output: 1,9,10


def find_intersection(str_list):
	new_list = sorted(str_list)
	new_string = ",".join(str_list)
	for i in str_list:
		if i in new_list[i]:
			new_string += i
		else:
			return False
	return new_list

print(find_intersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))


