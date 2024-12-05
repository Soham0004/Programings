numbers_str = input("Enter a list of numbers between 11 and 22 separated by spaces: ")
numbers = [int(num) for num in numbers_str.split()]
for i, num in enumerate(numbers):
  if num > 19:
    numbers[i] = 19
print("Modified list:", numbers)
