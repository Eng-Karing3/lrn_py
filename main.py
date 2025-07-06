from reminder_tools import messages, alerts

print(messages.motivation())
print(messages.reminder("Compelete your python project"))

hours = int(input("Enter current hour (0-23): "))
print(alerts.time_alert(hours))