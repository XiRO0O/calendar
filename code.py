import calendar

date = str(input('What are you looking for (day/month/year)? '))
print()

if date == 'day':
    y = int(input('Enter a year: '))
    m = int(input('Enter a month: '))
    d = int(input('Enter a day: '))
    if m <= 12:
        print(calendar.weekday(y, m, d))
    else:
        print("This month doesn't exist!")
    print()

elif date == 'month':
    y = int(input('Enter a year: '))
    m = int(input('Enter a month: '))
    print()
    if m <= 12:
        print(calendar.month(y, m))
    else:
        print("This month doesn't exist!")

elif date == 'year':
    y = int(input('Enter a year: '))
    print()
    print(calendar.calendar(y))

else:
    print("You need to choose: day, month or year - try again!")