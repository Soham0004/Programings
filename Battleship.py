import random
battlefield = [[random.randint(0, 1) for _ in range(5)] for _ in range(5)]
while True:
  try:
    row = int(input("Enter a row (1-5): ")) - 1
    column = int(input("Enter a column (1-5): ")) - 1

    if 0 <= row < 5 and 0 <= column < 5:
      if battlefield[row][column] == 1:
        print("Hit!")
      else:
        print("Miss!")
    else:
      print("Invalid row or column. Please try again.")
  except ValueError:
    print("Invalid input. Please enter integers only.")
