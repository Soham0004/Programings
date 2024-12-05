import random
numbers = range(1, 48)
winning_numbers = random.sample(numbers, 6)
winning_numbers.sort()
print("Winning lottery numbers:")
for number in winning_numbers:
  print(number)
