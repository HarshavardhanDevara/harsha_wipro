#timedelta Object
from datetime import datetime, timedelta

now = datetime.now()
print("Current date and time:", now)

# Add 1 day
tomorrow = now + timedelta(days=1)
print("This time tomorrow:", tomorrow)

# Subtract 1 week
last_week = now - timedelta(weeks=1)
print("This time last week:", last_week)