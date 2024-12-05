usernames_and_passwords = {
   "user1": "password1",
   "user2": "password2",
   "user3": "password3",
   "user4": "password4",
   "user5": "password5",
   "user6": "password6",
   "user7": "password7",
   "user8": "password8",
   "user9": "password9",
   "user10": "password10"
}
while True:
   username = input("Enter your username: ")
   password = input("Enter your password: ")
   if username not in usernames_and_passwords:
       print("Invalid username. Please try again.")
   elif password != usernames_and_passwords[username]:
       print("Invalid password. Please try again.")
   else:
       print("Login successful!")
       break
