import math
def area_of_square(side):
    area = side * side
    return area
def perimeter_of_square(side):
    perimeter = 4 * side
    return perimeter
side = float(input("Enter the side of the square: "))
square_area = area_of_square(side)
square_perimeter = perimeter_of_square(side)
print("Area of the square:", square_area)
print("Perimeter of the square:", square_perimeter)
