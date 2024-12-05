def is_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
def days_in_month(month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2 and is_leap_year(year):
        return 29
    else:
        return 28
year = int(input("Enter the year: "))
for month in range(1, 13):
    days = days_in_month(month, year)
    print(f"Month {month}: {days} days")
