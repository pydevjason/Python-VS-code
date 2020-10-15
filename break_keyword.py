# using the break keyword causes the program to break out of the loop and cease iteration.  In the case below as soon as the target number is found iteration stops and if there are any remaining elements in the list they are not iterated over.  

def target_number(num_list, number):
	for n in num_list:
		if number == n:
			break
	return number

numbers = [1,2,3,4,5,6,7]
print(target_number(numbers, 5))
