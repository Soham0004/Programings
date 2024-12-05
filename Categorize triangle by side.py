def check_triangle_validity(side1, side2, side3):
    if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
        return True
    else:
        return False
def categorize_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        triangle_type = "Equilateral"
    elif (side1 == side2) or (side2 == side3) or (side3 == side1):
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
    return triangle_type
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
if check_triangle_validity(side1, side2, side3):
    triangle_type = categorize_triangle(side1, side2, side3)
    print("Triangle type:", triangle_type)
else:
    print("The given side lengths are not valid for a triangle")
