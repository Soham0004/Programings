import random
matrix = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]
print("Matrix:")
for row in matrix:
  print(row)
largest_third_row = max(matrix[2])
print("Largest value in third row:", largest_third_row)
smallest_sixth_column = min(row[5] for row in matrix)
print("Smallest value in sixth column:", smallest_sixth_column)
