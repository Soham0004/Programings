import re
def validate_phone_number(phone_number):
  pattern = r"^(?:1-)?([2-9]\d{2})-([2-9]\d{2})-(\d{4})$"
  match = re.match(pattern, phone_number)
  return bool(match)
phone_numbers = [
  "1-301-447-5820",
  "301-447-5820",
  "301-4477-5820",
  "3X1-447-5820",
  "3014475820",
]
for phone_number in phone_numbers:
  valid = validate_phone_number(phone_number)
  print(f"{phone_number}: {'Valid' if valid else 'Invalid'}")
