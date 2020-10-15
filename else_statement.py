# if 20 > 15:
#     print("that is true")
# else:
#     print("that is false")
    
    

# while True:
#     num = int(input("Enter a random number: "))
#     if num < 1_000_000:
#         print("come on man! thats small time thinking!")
#         continue
#     else:
#         print("Ma Nigga!... thats what I'm talkin bout!")
#         num = False
        
#     break

def calc(operation, a, b):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "you must enter either +, -, *, or /"
    
print(calc("/", 2, 2))