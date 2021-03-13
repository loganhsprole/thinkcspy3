current_time = int(input("Current time: "))
hours_to_wait = int(input("Hours to wait: "))

alarm_time = (current_time + hours_to_wait) % 24

print(alarm_time, ":00")
