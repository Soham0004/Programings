import random

# List of team names from Team 1 to Team 16
teams = [f"Team {i}" for i in range(1, 17)]

# Randomly select a team
selected_team = random.choice(teams)

# Print the randomly selected team
print("Selected team:", selected_team)
