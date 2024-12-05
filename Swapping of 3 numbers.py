def swap_three_variables(x, y, z):
 temp = x
 x = y
 y = z
 z = temp
 return x, y, z
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
z = int(input("Enter the value of z: "))
x, y, z = swap_three_variables(x, y, z)
print("After swapping:")
print("x =", x)
print("y =", y)
print("z =", z)
