x = 10

def change_x():
    x = 15
    
print(x)
change_x()
print(x)
print()

# Define a global "a" variable assigned to the value 1


# Declare a "modify_a" function that accepts a single argument.
# It should overwrite the value of the a global variable with the argument
a = 1
def modify_a(value):
    global a
    a = value

print(a)
modify_a(2)
print(a)
