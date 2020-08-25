# Using the workspace:

# Here are a few tips orienting you to this kind of workspace.

# In the top panel is a code editor where you can edit the Python file user_input_numlist.py. Scroll up and down in this panel to see all the code. You can also expand or shrink this panel by clicking and dragging its bottom border.

# In the bottom panel, you can execute your Python file by clicking on New Terminal and entering python user_input_numlist.py on the command line.

# The solutions have been provided on the next page, but I encourage you to try figuring out where the bug is in the code, and fixing it yourself.

# Sample Output: This is what the output should look like.

# >>> user_list: [23, 24, 25, 26, 27, 28, 29, 30, 31, 22]
# >>> The sum of the even numbers in user_list is: 130.

# initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0

# seek user input for ten numbers 
for i in range(10):
    userInput = input("Enter any 2-digit number: ")
    
# check to see if number is even and if yes, add to list_sum
# print incorrect value warning  when ValueError exception occurs
    try:
        number = userInput
        user_list.append(number)
        if number % 2 == 0:
            list_sum += number
    except ValueError:
        print("Incorrect value. That's not an int!")
        