import calendar

year = 2024
month = 2

#matrix format
cal = calendar.monthcalendar(year, month)

print("Mo  Tu  We  Th  Fr  Sa  Su")

for week in cal:
    for day in week:
        if day == 0:
            print("   ", end=" ")
        else:
            print(f"{day:2} ", end=" ")
    print()
