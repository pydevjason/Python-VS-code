# returns a set of elements that are not shared by 2 sets

# example
candy_bars = {"Milky Way", "Snickers", "100 Grand"}
sweet_things = {"Sour Patch Kids", "Reeses Pieces", "Snickers"}

print(candy_bars.symmetric_difference(sweet_things))
print()
# short_hand syntax is the caret symbol ^
print(candy_bars ^ sweet_things)
print(sweet_things ^ candy_bars)
print()

gatorade_flavors = { "blue", "red", "orange" }
powerade_flavors = { "red", "green", "yellow" }
print(gatorade_flavors.symmetric_difference(powerade_flavors))
print()

juice_flavors = { "Lemon", "Peach", "Raspberry", "Apple" }
tea_flavors = { "Peach", "Grape", "apple" }
print(juice_flavors ^ tea_flavors)