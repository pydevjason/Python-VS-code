#  example 1 using for loop
def fizz_buzz(number):
    current_number = 1
    for k in range(current_number, number):
        if current_number % 3 == 0 and current_number % 5 == 0:
            print("FizzBuzz")
        elif current_number % 5 == 0:
            print("Buzz")
        elif current_number % 3 == 0:
            print("Fizz")
        else:
            print(current_number) 
        current_number += 1
    
fizz_buzz(31)

print()
print()

# example 2 using while loop
def fizz_buzz2(ending_number):
    current_number = 1
    while current_number <= ending_number:
        if current_number % 3 == 0 and current_number % 5 == 0:
            print("FizzBuzz")
        elif current_number % 5 == 0:
            print("Buzz")
        elif current_number % 3 == 0:
            print("Fizz")
        else:
            print(current_number) 
        current_number += 1
        
fizz_buzz2(30)
