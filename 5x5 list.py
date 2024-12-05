import random
list5x5 = [[random.randint(0, 1) for _ in range(5)] for _ in range(5)]
zero_coordinates = [(i, j) for i in range(5) for j in range(5) if list5x5[i][j] == 0]
if zero_coordinates:
    random_coordinate = random.choice(zero_coordinates)
    row, col = random_coordinate
    list5x5[row][col] = 1
    for row in list5x5:
        print(row)
else:
    print("All entries are one.")
