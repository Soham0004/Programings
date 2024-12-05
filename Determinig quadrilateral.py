def determine_quadrilateral_type(side1, side2, side3, side4, angle):
    if side1 == side2 == side3 == side4 and angle == 90:
        print("The quadrilateral is a square")
        return
    if side1 == side2 == side3 == side4 and angle != 90:
        print("The quadrilateral is a rhombus")
        return
    if side1 == side3 and side2 == side4 and angle != 90:
        print("The quadrilateral is a parallelogram")
        return
    print("The quadrilateral is irregular")
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
side4 = float(input("Enter the length of side 4: "))
angle = float(input("Enter the internal angle: "))
determine_quadrilateral_type(side1, side2, side3, side4, angle)
