def get_4x4_list_from_user():
  """Prompts the user to enter a 4x4 list of integers."""
  matrix = []
  for i in range(4):
    row = input(f"Enter row {i+1} (separated by spaces): ").split()
    row = [int(num) for num in row]
    if len(row) != 4:
      raise ValueError("Invalid input: Each row must contain 4 numbers.")
    matrix.append(row)
  return matrix
def calculate_average(matrix):
  """Calculates the average of all entries in a 4x4 list."""
  total_sum = sum(sum(row) for row in matrix)
  num_entries = len(matrix) * len(matrix[0])
  average = total_sum / num_entries
  return average
try:
  matrix = get_4x4_list_from_user()
  average = calculate_average(matrix)
  print("Average of all entries:", average)
except ValueError as e:
  print(e)
