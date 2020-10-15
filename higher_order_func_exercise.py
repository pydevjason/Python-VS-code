# Define an "outer" function that accepts no arguments
# Inside the body of "outer", define an "inner" function
# The "inner" function should return the value 5.
# From "outer", return the uninvoked "inner" function

def outer_function():
    def inner_function():
        return 5
    return inner_function
print(outer_function())
print(outer_function()())