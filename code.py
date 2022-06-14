import calendar

date = str(input('What are you looking for (month/year)? '))

y = int(input('Enter a year: '))
m = int(input('Enter a month: '))

print()
if m <= 12:
    print(calendar.month(y, m))
else:
    print("This month doesn't exist!")