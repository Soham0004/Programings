def categorize_triangle(angle1, angle2, angle3):
    if angle1 + angle2 + angle3 != 180:
        return "Invalid triangle"
    if angle1 == angle2 == angle3:
        return "Equilateral"
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        return "Right-angled"
    if angle1 < 90 and angle2 < 90 and angle3 < 90:
        return "Acute-angled"
    return "Obtuse-angled"
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))
triangle_category = categorize_triangle(angle1, angle2, angle3)
print(triangle_category)
