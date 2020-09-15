# scope - the locations in a program in which a name can be used
# a variable that is defined outside of any function is in the global scope
# variables inside a function are either enclosing or local variable

# example, here we can see that age from inside the function can reach the global age variable

age = 41
def scope():
    print(age)
    
scope()
print()

# shadow variable: a local variable that shares the same name as a global variable.  Generally this is not a good idea and you should have different names for variables in the global and local scope as this can cause confusion

def scope2():
    age = 100
    print(age)
    
scope2()
print(age)

# a constant is a name for a value that does not change over the programs execution.  constants are written in all caps to show the difference between a constant and a variable 

TAX_RATE = 0.06

def calculate_tax(price):
    return f"{price * TAX_RATE:.2f}" 

def calculate_tip(price):
    return f"{price * (TAX_RATE * 3):.2f}"

print(calculate_tax(10))
print(calculate_tip(10))

