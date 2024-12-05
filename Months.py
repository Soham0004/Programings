months = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}
while True:
  month_name = input("Enter a month name (or 'quit' to exit): ").lower()
  if month_name == "quit":
    break
  matching_month = [name for name in months.keys() if name.lower().startswith(month_name[:3])]
  if matching_month:
    month_name = matching_month[0] 
    print(f"{month_name} has {months[month_name]} days.")
  else:
    print("Month name not found.")
print("\nMonths in alphabetical order:")
for month in sorted(months.keys()):
  print(month)
print("\nMonths with 31 days:")
for month, days in months.items():
  if days == 31:
    print(month)
print("\nMonths sorted by number of days:")
for month, days in sorted(months.items(), key=lambda item: item[1]):
  print(f"{month}: {days} days")
