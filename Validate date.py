from datetime import datetime
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
user_input = input("Enter a date (YYYY-MM-DD): ")
if is_valid_date(user_input):
    print("Valid date!")
else:
    print("Invalid date.")
