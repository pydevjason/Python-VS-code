from datetime import date, time, datetime
# as a reminder, datetime objects are immutable 
print(datetime(1999, 7, 24))
print(datetime(1999, 7, 24, 14))
print(datetime(1999, 7, 24, 14, 16))
print(datetime(1999, 7, 24, 14, 16, 58))
print(datetime(year = 1999, month = 7, day = 24, hour = 14, minute = 16, second = 58))

today = datetime.today()
print(today)
print(datetime.now())
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)
print(today.second)
# the weekday class method returns the day of the week through a 0 based index starting at Monday with an index of 0
print(today.weekday())
print()

same_time_twenty_years_ago = today.replace(year = 1999)
print(same_time_twenty_years_ago)
print()

# Define a one_from_two function that accepts a date object and a time object
# It should return a datetime object consisting of 
#     - the year, month and day from the date object 
#     - the hour, minutes, and seconds from the time object
#
# EXAMPLE:
#
# from datetime import date, time, datetime


def one_from_two(some_date, some_time):
	year = some_date.year
	month = some_date.month
	day = some_date.day

	hour = some_time.hour
	minute = some_time.minute
	second = some_time.second

	return datetime(year, month, day, hour, minute, second)

some_date = date(2002, 2, 22)
some_time = time(9, 45, 23)
print(one_from_two(some_date, some_time))


# => datetime object representing 2002-02-22 09:45:23


























