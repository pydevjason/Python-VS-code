# while loops execute a block of code as long as a certain condition remains True.  If at any point the condition becomes False the while loop ends.
# beware the INFINITE LOOP, code that continues to run because of no condition evaluating to False

# example 1
# count = 0
# while count <= 5:
#     print(count)
#     count += 1
    
# example 2
# while True:
#     number = int(input("Enter a number greater than 10: "))
#     if number > 10:
#         print(f"Congratulations! You know that {number} > 10")
#         break
#     else:
#         print(f"Sorry, {number} is not greater than 10.")
        

# example 3
invalid_number = True
while invalid_number:
    user_value = int(input("Enter a number greater than 10: "))
    if user_value > 10:
        print(f"That's right! {user_value} > 10")
        invalid_number = False
    else:
        print(f"Sorry, {user_value} is not greater than 10")