# Given the tuple below, destructure the three values and
# assign them to position, city and salary variables
# Do NOT use index positions (i.e. job_opening[1])
job_opening = ("Software Engineer", "New York City", 100000)
position, city, salary = job_opening
print(job_opening)

print()
# Given the tuple below, 
# - destructure the first value and assign it to a street variable
# - destructure the last value and assign it to a zip_code variable
# - destructure the middle two values into a list and assign it to a city_and_state variable
address = ("35 Elm Street", "San Francisco", "CA", "94107")
street, *city_and_state, zip_code = address
print(address)

# Declare a sum_of_evens_and_odds function that accepts a tuple of numbers.
# It should return a tuple with two numeric values:
# -- the sum of the even numbers
# -- the sum of the odd numbers.
#
# sum_of_evens_and_odds((1, 2, 3, 4))   => (6, 4)
# sum_of_evens_and_odds((1, 3, 5))      => (0, 9)
# sum_of_evens_and_odds((2, 4, 6))      => (12, 0)

def sum_of_evens_and_odds(tup_sequence):
    even = 0
    odd = 0
    for i in tup_sequence:
        if i % 2 == 0:
            even += i
        else:
            odd += i
    return even, odd

print(sum_of_evens_and_odds((1,3,5)))
            