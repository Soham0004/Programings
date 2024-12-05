def count_unique_values(input_list):
  unique_values = set(input_list)
  frequencies = []
  for value in unique_values:
    count = input_list.count(value)
    frequencies.append((value, count))
  return frequencies
input_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
frequencies = count_unique_values(input_list)
print("Unique values and their frequencies:")
for value, count in frequencies:
  print(f"{value}: {count}")
