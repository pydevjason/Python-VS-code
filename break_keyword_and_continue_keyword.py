# using the break keyword causes the program to break out of the loop and cease iteration.  In the case below as soon as the target number is found iteration stops and if there are any remaining elements in the list they are not iterated over.  

def target_number(num_list, number):
	for n in num_list:
		if number == n:
			break
	return number

numbers = [1,2,3,4,5,6,7]
print(target_number(numbers, 5))

print()
# the continue keyword causes the loop to move onto the next iteration automatically.  it does not terminate the loop, just the current iteration of the loop

# create a function that accepts a list of numbers and return all positive values in the list.

def positive_numbers(num_list):
	pos_nums = []
	for k in num_list:
		if k > 0:
			pos_nums.append(k)
	return pos_nums

print(positive_numbers([-3,2,-78,4,9]))

print()
# create a function that accepts a list of numbers and return the sum of all positive values in the list.

def sum_positive_numbers(num_list):
	total = 0
	for i in num_list:
		if i > 0:
			total += i
	return total

print(sum_positive_numbers([-1,2,-3,4,-5,6]))

print()

# now using the continue keyword on def sum_positive_numbers.
def sum_positive_numbers2(num_list):
	total = 0
	for i in num_list:
		if i < 0:
			continue
		total += i
	return total

print(sum_positive_numbers2([-1,2,-3,4,-5,6]))