import random
def simulate_lottery_drawings():
 """Simulates lottery drawings until the user's numbers are picked."""
 user_numbers = random.sample(range(1, 11), 6)
 drawing_count = 0
 while True:
   drawing_count += 1
   drawn_numbers = random.sample(range(1, 11), 6)
   if drawn_numbers == user_numbers:
     break
 return drawing_count
total_drawings = 0
for _ in range(1000):
 total_drawings += simulate_lottery_drawings()
average_drawings = total_drawings / 1000
print("Average number of drawings needed:", average_drawings)
