# returns a new set of elements that are exclusive to 1 of the 2 sets

# example
candy_bars = {"Milky Way", "Snickers", "100 Grand"}
sweet_things = {"Sour Patch Kids", "Reeses Pieces", "Snickers"}

print(candy_bars.difference(sweet_things))

# short-hand syntax is using the - minus
print(candy_bars - sweet_things) 
print(sweet_things - candy_bars)
print()

gatorade_flavors = { "blue", "red", "orange" }
powerade_flavors = { "red", "green", "yellow" }
 
print(gatorade_flavors.difference(powerade_flavors))
print()

# These are all the strings found in juice_flavors that are NOT contained in tea_flavors.
juice_flavors = { "Lemon", "Peach", "Raspberry", "Apple" }
tea_flavors = { "Peach", "Grape", "apple" }
print(juice_flavors - tea_flavors)


