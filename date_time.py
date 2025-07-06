import datetime

today = datetime.datetime.now()
print(f"Today is {today.strftime('%A, %d %B %Y')}")

# Reminder
deadline = datetime.datetime(2025, 7, 1)
days_left = (deadline - today).days
print(f"You have {days_left} days to hit your next Python milestone!")
