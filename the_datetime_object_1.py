from datetime import datetime
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
