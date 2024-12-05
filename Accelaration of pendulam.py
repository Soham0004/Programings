import math
l = float(input("Enter the effective length of the pendulum in meters: "))
T = float(input("Enter the period of the pendulum in seconds: "))
g = 4 * math.pi * math.pi * l / (T * T)
print("The acceleration due to gravity is:", g, "m/s^2")
