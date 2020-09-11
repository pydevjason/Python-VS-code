# the .union() method combines the elements from both sets.  The combination of all elements.  Again since we are dealing with sets all duplicate values are removed 

candy_bars = {"Milky Way", "Snickers", "100 Grand"}
sweet_things = {"Sour Patch Kids", "Reeses Pieces", "Snickers"}

print(candy_bars.union(sweet_things))
print()
print(sweet_things.union(candy_bars))
print()

# the shorthand syntax for the union method is the | vertical pipe
print(sweet_things | candy_bars)
print()

juice_flavors = { "Lemon", "Peach", "Raspberry", "Apple" }
tea_flavors = { "Peach", "Grape", "apple" }
print(juice_flavors | tea_flavors)