import calendar

date = str(input('What are you looking for (month/year)? '))

if date == 'month':
    y = (input('Enter a year: '))
    m = (input('Enter a month: '))
    print()
    if m != int:
        print('You need to choose number!')
    elif m <= 12:
        print(calendar.month(y, m))
    else:
        print("This month doesn't exist!")

elif date == 'year':
    y = (input('Enter a year: '))
    print()
    print(calendar.calendar(y))

else:
    print("You need to choose: month or year - try again!")