from datetime import date
from datetime import time

start = time()
print(start)
print(type(start))
print(start.hour)
print(start.minute)
print(start.second)
print()
# that is 6 in the morning
print(time(6))
print(time(hour = 6))
print(time(hour = 18))
print(time(12, 25))
print(time(hour = 7, minute = 7, second = 7))
print("\n")

# Declare a titanic variable pointing to a date object representing April 14th, 1912
# Declare an independence_day variable pointing to a date object representing July 4th, 1776
# Declare an alarm_clock variable set to a time object representing 05:45:00AM
# Declare a one_second_away variable set to a time object representing 11:59:59PM

titanic = date(1912, 4, 14)
independence_day = date(1776, 7, 4)
alarm_clock = time(5, 45)
one_second_away = time(23, 59, 59)


















