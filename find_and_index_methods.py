# methods are functions that act upon specific objects.  They are connected directly to an object.  They can accept arguments and return values.  

# the .find() returns the lowest index in a string where a substring is found.  will return an integer for the index position of a substring

browser = "Google Chrome"

# 7 is the index position of the first identifies C element in the string Google Chrome
print(browser.find("C"))
print(browser.find("Ch"))
print(browser.find("o"))
print(browser.find("G"))

# -1 is returned if a value is not found 
print(browser.find("Z"))
print(browser.find("Zxy"))
print(browser.find("c"))
print()

# .find() also accepts a second argument, an int for the starting index position of your choice

print(browser.find("o"))
print(browser.find("o", 2))
print(browser.find("o", 5))

# .index() is a complimentary method to .find()  It works the exact same way as .find() with the only difference being that if a value is not found in a string it will raise a ValueError
print()
print(browser.index("C"))
# print(browser.index("Z"))