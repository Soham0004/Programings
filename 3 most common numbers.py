import random
numbers_list = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]
number_counts = {}
for row in numbers_list:
 for number in row:
   if number not in number_counts:
     number_counts[number] = 0
   number_counts[number] += 1
most_common_numbers = sorted(number_counts.items(), key=lambda item: item[1], reverse=True)[:3]
print("Number counts:", number_counts)
print("Three most common numbers:", most_common_numbers)
