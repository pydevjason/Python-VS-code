# any number that is not 0 is truthy and any string that is not empty is truthy 
# 0 is falsey and "" is falsey
# these things are neither True or False, but they evaluate to a concept of truthiness and falsiness.

# example 1 is falsey
if 0:
    print("hello")
else:
    print("goodbye")
    
# examle 2 is truthy
if 3:
    print("3 is truthy")
else:
    print("What !?")
    
# example 3 string is truthy
if "hello":
    print("hello is truthy")

# example 4 is falsey:
if "":
    print("this will never print")
    
print()

print(bool(1))
print(bool(0))
print(bool(""))
print(bool("hello"))
