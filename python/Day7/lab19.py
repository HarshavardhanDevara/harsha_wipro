#datetime Module
from datetime import datetime, date, time

# Current date and time
now = datetime.now()
print("Current date and time:", now)

# Creating a specific date
my_birthday = date(2000, 2, 18)
print("My birthday:", my_birthday)

# Creating a specific time
alarm = time(4, 30, 0)
print("Alarm set for:", alarm)