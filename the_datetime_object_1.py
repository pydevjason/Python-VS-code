from datetime import datetime

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
