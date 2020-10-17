# a duration or the passage of time

from datetime import datetime, timedelta

my_birthday = datetime(1978, 2, 10)
today = datetime.now()

my_lifespan = today - my_birthday
print(my_lifespan)
print(type(my_lifespan))
print(my_lifespan.total_seconds())
print()

five_hundred_days = timedelta(days = 500, hours = 12)
print(five_hundred_days)
print(five_hundred_days * 2)
print(today + five_hundred_days)

release_date = datetime(2004, 11, 24, 4, 14, 25)
print(release_date.replace(2010, 6, 4))
