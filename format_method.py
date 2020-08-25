# the arguments can be passed by relative position, numeric position, or by keyword arguments.

# here using relative position
# mad_libs = "{} ran down the river and {} up the {}."
# print(mad_libs.format("Ethan", "swam", "street"))

# print()

# passing arguments by numeric position
# mad_libs = "{0} ran down the river and {1} up the {2}."
# print(mad_libs.format("Ethan", "swam", "street"))
# print(mad_libs.format("Jason", "flew", "house"))

# print()

# using keyword parameters
mad_libs = "{name} ran down the river and {action} up the {thing}."
# print(mad_libs.format(name = "Ethan", verb = "swam", noun = "street"))
# print(mad_libs.format(name = "Jason", verb = "flew", noun = "house"))

name = input("Enter a name: ")
action = input("Enter an action: ")
thing = input("Enter a thing: ")
print("Now this is what I say ->")
print(mad_libs.format(name = name, action = action, thing = thing))