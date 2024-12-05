teams_data = {}
while True:
  team_name = input("Enter a team name (or 'done' to finish): ")
  if team_name == "done":
    break
  wins = int(input("Enter the number of wins: "))
  losses = int(input("Enter the number of losses: "))
  teams_data[team_name] = [wins, losses]
while True:
  team_name = input("\nEnter a team name to check its winning percentage (or 'quit' to exit): ")
  if team_name == "quit":
    break
  if team_name in teams_data:
    wins, losses = teams_data[team_name]
    winning_percentage = wins / (wins + losses) * 100
    print(f"{team_name}'s winning percentage: {winning_percentage:.2f}%")
  else:
    print(f"Team '{team_name}' not found.")
wins_list = [stats[0] for stats in teams_data.values()]
print("\nList of wins:", wins_list)
winning_teams = [team for team, stats in teams_data.items() if stats[0] > stats[1]]
print("\nTeams with winning records:", winning_teams)
