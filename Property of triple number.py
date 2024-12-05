for i in range(1, 999):
  middle_number = i + 1
  product = i * (i + 2)
  square = middle_number ** 2
  if square == product + 1:
    print(f"{i}, {middle_number}, {i + 2}")
