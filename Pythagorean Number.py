from math import sqrt
for z in range(1, 100):
  for x in range(1, z):
    y = sqrt(z**2 - x**2)
    if y.is_integer():
      print(f"(X, Y, Z) = ({int(x)}, {int(y)}, {z})")
