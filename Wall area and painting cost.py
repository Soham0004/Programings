length = float(input("Enter the length of the room: "))
width = float(input("Enter the width of the room: "))
height = float(input("Enter the height of the room: "))
wall_area = 2 * height * (length + width)
charge_per_unit = float(input("Enter the charge per square unit: "))
total_cost = wall_area * charge_per_unit
print("Area of the walls is:", wall_area)
print("Total cost of painting:", total_cost)
