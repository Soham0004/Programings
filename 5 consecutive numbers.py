for i in range(1, 996):  # Iterate up to 996 to account for series within 1000
  sum_of_squares_first_three = i**2 + (i + 1)**2 + (i + 2)**2
  sum_of_squares_last_two = (i + 3)**2 + (i + 4)**2
  if sum_of_squares_first_three == sum_of_squares_last_two:
    print(f"{i}, {i + 1}, {i + 2}, {i + 3}, {i + 4}")

