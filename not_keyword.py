# the not keyword takes the inverse of a boolean

print(not True)
print(not False)

print()
if "H" in "Hello":
    print("It's true, H is in the string 'Hello'")
    
print()
if "Z" not in "Hello":
    print("It's true, Z is not in Hello")
    
print()
# always remember, not keyword is simply a negation
value = 10
if not value > 100:
    print("It's true, 10 is not greater than 100")