"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


def next_weekday(current_weekday):
    return (current_weekday + 1) % 7


def next_year_month_day(current_year_month_day):
    year = current_year_month_day[0]
    month = current_year_month_day[1]
    day = current_year_month_day[2]

    if month in [1, 3, 5, 7, 8, 10] and day == 31:
        return [year, month + 1, 1]
    if month in [4, 6, 9, 11] and day == 30:
        return [year, month + 1, 1]

    if month == 2:
        if day == 29:
            return [year, 3, 1]
        if day == 28:
            if year % 4 == 0 and year % 400 != 0:
                return [year, 2, 29]
            else:
                return [year, 3, 1]

    if month == 12 and day == 31:
        return [year + 1, 1, 1]

    return [year, month, day + 1]


year_month_date = [1901, 1, 1]
weekday = 1
sunday_on_the_first_count = 0

while year_month_date != [2001, 1, 1]:
    if year_month_date[2] == 1 and weekday == 6:
        # print(
        #     f"{year_month_date[0]} {year_month_date[1]} {year_month_date[2]} {weekday}"
        # )
        sunday_on_the_first_count += 1
    weekday = next_weekday(weekday)
    year_month_date = next_year_month_day(year_month_date)

print(sunday_on_the_first_count)
