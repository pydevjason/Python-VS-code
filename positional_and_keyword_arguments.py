def add(a, b): # a and b are positional arguments
    print(f"the sum of {a} + {b} is {a + b}")

# add(3,4) 
add(a = 4, b = 6) # keyword args are placed after the = for being explicit 

def add_three(a, b, c):
    print(f"The sum of the three numbers is {a + b + c}")

add_three(5, 10, 15) # using positional arguments
add_three(a = 5, b = 10, c = 15) # using keyword args