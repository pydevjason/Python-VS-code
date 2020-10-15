# using this approach technically does not return anything to the world outside of the function
def add(a, b):
    print(a + b)

result = add(3, 5)
print(result)

# a return value returns an output from a function
# example 

def add_two(a, b):
    return a + b

print(add_two(2,4))

# the return statement concludes the function.  No code will ever be reached after the return statement 