import random
def draw_name_from_hat(names, entries):
 """Simulates drawing a name from a hat with varying entry counts."""
 hat = []
 for name, count in zip(names, entries):
   hat.extend([name] * count)
 winner = random.choice(hat)
 return winner
names = input("Enter a list of names separated by commas: ").split(",")
entries_str = input("Enter the number of entries for each person, separated by commas: ").split(",")
entries = [int(entry) for entry in entries_str]
if len(names) != len(entries):
 print("Error: The number of names and entry counts must be the same.")
else:
 winner = draw_name_from_hat(names, entries)
 print("The winner is:", winner)
