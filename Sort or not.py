def is_sorted(my_list):
  if len(my_list) <= 1:
    return True
  for i in range(len(my_list) - 1):
    if my_list[i] > my_list[i + 1]:
      return False
  return True
numbers = input("Enter a list of numbers separated by spaces: ")
my_list = [int(num) for num in numbers.split()]
if is_sorted(my_list):
  print("The list is sorted.")
else:
  print("The list is not sorted.")
