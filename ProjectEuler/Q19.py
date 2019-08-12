"""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""

def weekday_shift(month, year):
    if(month == 2):
        if(year%400 == 0 or (year%4 == 0 and year%100 != 0)):
            return 1
        return 0
    if(month in [4, 6, 9, 11]):
        return 2
    return 3

def first_of_month(month, year):
    if(month == 2 and year == 1983):
        return 2
    elif(month == 1 and year == 1900):
        return 1
    elif(month > 1):
        return (weekday_shift(month - 1, year) + first_of_month(month - 1, year))%7
    else:
        return (weekday_shift(12, year - 1) + first_of_month(12, year - 1))%7
