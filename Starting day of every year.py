import calendar
def starting_day_of_year(year):
    starting_day = calendar.weekday(year, 1, 1)
    day_name = calendar.day_name[starting_day]
    return day_name
year_input = int(input("Enter the year: "))
starting_day = starting_day_of_year(year_input)
print(f"The starting day of {year_input} is: {starting_day}")
