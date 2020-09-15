# higher order functions are functions that either accept a function as an argument or return a function as a return value


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# calculate is the higher order function in this case that takes in either add or subtract functions and returns the value for the function that was taken in through calculate 
def calculate(func, a, b):
    return func(a, b)

print(calculate(subtract, 8, 2))

# Define an invoke_thrice function.
# It should accept a single argument (which will be a function)
# In its body, the invoke_thrice function should invoke
# the function that's passed in exactly three times.

def invoke_thrice(func):
    func()
    func()
    func()
    
def sample_func():
    print("abc")

invoke_thrice(sample_func)
    


