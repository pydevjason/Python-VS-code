# returns a new set of elements in common from 2 separate sets

candy_bars = {"Milky Way", "Snickers", "100 Grand"}
sweet_things = {"Sour Patch Kids", "Reeses Pieces", "Snickers"}

print(candy_bars.intersection(sweet_things))

# ampersand & is short-hand syntax for the intersection method

print(candy_bars & sweet_things)
print()
# example 2

values = {3.0, 4.0, 5.0}
more_values = {3, 4, 5, 6}

print(values.intersection(more_values))
print(values & more_values)
print(more_values.intersection(values))
print()

juice_flavors = { "Lemon", "Peach", "Raspberry", "Apple" }
tea_flavors = { "Peach", "Grape", "apple" }
 
print(juice_flavors & tea_flavors)

