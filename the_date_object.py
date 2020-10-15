# date and time objects are immutable 
# date is a constructor much like a list or dict, a class that returns to you a new object, the constructor for a date object accepts 3 int arguments all of which are required 
from datetime import date

my_birthday = date(1978, 10, 2)
print(my_birthday)
print(type(my_birthday))

moon_landing = date(year = 1969, month = 7, day = 20)
print(moon_landing)

print(my_birthday.year)
print(my_birthday.month)
print(my_birthday.day)
print()

today = date.today()
print(today)