def remove_duplicates(my_list):
  unique_elements = []
  seen_elements = set()
  for element in my_list:
    if element not in seen_elements:
      unique_elements.append(element)
      seen_elements.add(element)
  return unique_elements
numbers_str = input("Enter a list of numbers separated by spaces: ")
my_list = [int(num) for num in numbers_str.split()]
unique_list = remove_duplicates(my_list)
print("List with duplicates removed:", unique_list)
