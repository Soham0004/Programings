import math
radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))
slant_height = math.sqrt(radius**2 + height**2)
base_area = math.pi * radius**2
surface_area = math.pi * radius * slant_height
total_area = base_area + surface_area
print("Total surface area of the cone:", total_area)
