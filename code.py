import calendar

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))

print()
if month <= 12:
    print(calendar.month(year, month))
else:
    print("This month doesn't exist!")