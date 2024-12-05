import random
num_simulations = 10000
roll_counts = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
for _ in range(num_simulations):
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  roll_sum = die1 + die2
  roll_counts[roll_sum] += 1
for roll_sum, count in roll_counts.items():
  percentage = (count / num_simulations) * 100
  print(f"Roll {roll_sum}: {percentage:.2f}%")
