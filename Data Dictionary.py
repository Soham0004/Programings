def process_user_data(user_data):
  print("Users whose phone number ends in 8:")
  for user in user_data:
    if user["phone"].endswith("8"):
      print(user["name"])
  print("\nUsers without an email address listed:")
  for user in user_data:
    if not user["email"]:
      print(user["name"])
user_data = [
  {'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
  {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
  {'name': 'Princess', 'phone': '555-3141', 'email': ''},
  {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}
]
process_user_data(user_data)
