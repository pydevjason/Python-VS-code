# decorator is a higher order function that accepts a function and returns another function as an output.  decorators add additional functionality to functions.  So a higher order function retains its original capabilities plus additional features.  

# example

def be_nice(fn):
    def inner():
        print("I will execute your function for you....\n")
        fn()
        print("Function execution completed. Have a nice day.")
        
    return inner 

# there is also a syntactic sugar way of expressing the decorator using the @ symbol
@be_nice
def complex_business_logic():
    print("doing complex things....\n")

complex_business_logic()

# output = be_nice(complex_business_logic)
# output()
import functools



def uppercase(fn):

    @functools.wraps(fn)

    def wrapper(*args, **kwargs):

        fn(*args, **kwargs).upper()



    return wrapper



@uppercase
def concatenate(a, b):

    """Combines two strings together"""

    return a + b



print(concatenate("pyt", "hon"))


