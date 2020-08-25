# create a add_odd_numbers function that accepts a list of numbers and have it return the total sum

def add_odd_numbers(num_list):
	total = 0
	for i in num_list:
		if i % 2 == 1:
			total += i
	return total

print(add_odd_numbers([1, 2, 3, 4, 5, 6]))


# create a greatest_number function that accepts a list of numbers and returns the greatest number from the list.

def greatest_number(num_list):
	high_num = num_list[0]
	for i in num_list:
		if i > high_num:
			high_num = i
	return high_num

print(greatest_number([-2, -45, -6, -1, 0]))
print(greatest_number([23, 2, 9, 78, 18, 55]))