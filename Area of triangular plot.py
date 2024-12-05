def perimeter_of_triangle(side1, side2, side3):
    perimeter = side1 + side2 + side3
    return perimeter
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
triangle_perimeter = perimeter_of_triangle(side1, side2, side3)
print("Perimeter of the triangle:", triangle_perimeter)
