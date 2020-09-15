# using this example:
# convert gallons to cups

# 1 gallon = 4 quarts
# 4 quarts = 2 pints
# 1 pints = 2 cups

def gallons_to_cups(gallons):
    def gallons_to_quarts(gallons):
        print(f"converting {gallons} gallons to quarts.")
        return gallons * 4
    
    def quarts_to_pints(quarts):
        print(f"converting {quarts} quarts to pints.")
        return quarts * 2
    
    def pints_to_cups(pints):
        print(f"converting {pints} pints to cups.")
        return pints * 2
    
    quarts = gallons_to_quarts(gallons)
    pints = quarts_to_pints(quarts)
    cups = pints_to_cups(pints)
    
    return f"There are {cups} cups in {gallons} gallons\n"

print(gallons_to_cups(1))
print(gallons_to_cups(3))