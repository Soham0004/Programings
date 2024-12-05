def left_to_right_representation(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    flat_list = [matrix[i][j] for i in range(rows) for j in range(cols)]
    return flat_list
def right_to_left_representation(flat_list, rows, cols):
    matrix = [[flat_list[i * cols + j] for j in range(cols)] for i in range(rows)]
    return matrix
matrix_left = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
flat_list = left_to_right_representation(matrix_left)
print("Left to Right Representation:", flat_list)
rows = 3
cols = 3
matrix_right = right_to_left_representation(flat_list, rows, cols)
print("Right to Left Representation:")
for row in matrix_right:
    print(row)
