# a lambda() function is an anonymous function.  A function without name.  They are meant to be used once and then discarded.  They are used well with functions like filter and map.

# using lambda to check if an element length is greater than 5
metals = ["gold", "silver", "platinum", "palladium"]

print(list(filter(lambda i: len(i) > 5, metals)))
print(list(filter(lambda j: "p" in j, metals)))

# using map count how many times the letter 'l' appears in each element
print(list(map(lambda k: k.count("l"), metals)))

# return a new list where the lowercase 's' is replaced with $
print(list(map(lambda x: x.replace("s", "$"), metals)))