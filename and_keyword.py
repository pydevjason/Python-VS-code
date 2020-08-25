# when using the 'and' keyword both conditions must be true for the statement to evaluate to True.  If even one of them is false the whole thing evaluates to False.

# example 1 evaluates to True
if 5 < 7 and "rain" == "rain":
    print("These are both true.")
    
# example 2 evaluates to False
if 5 < 5 and "Rain" == "rain":
    print("This is true.")
else:
    print("This is false.")

# example 3 both statements evaluate to True   
value = 95
if value > 90 and value < 100:
    print("95 is greater than 90 and less than 100")