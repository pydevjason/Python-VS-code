color1 = "regre"
color2 = "rere"

# the only way the nested if statement will execute is if the first if statement evaluates to True
if color1 == "red":
    if color2 == "blue":
        print("red and blue")
    else:
        print("still red but not blue")
else:
    print("color 1 should be red to reach the nested if statement")
    
print()

if color1 == "red" and color2 == "blue":
    print("Both these statements are true.")
elif color1 == "red":
    print("red only")
else: 
    print("neither red nor blue here")

print()

print(True and True and False)