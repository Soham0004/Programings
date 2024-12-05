import random
random_list = [random.randint(0, 1) for _ in range(100)]
print("Generated integers:", random_list)
longest_run = 0
current_run = 0
for num in random_list:
  if num == 0:
    current_run += 1
  else:
    longest_run = max(longest_run, current_run)
    current_run = 0
longest_run = max(longest_run, current_run)
print(f"Longest run of zeros: {longest_run}")
