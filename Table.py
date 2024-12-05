n = int(input("Enter the number for which you want to generate a table: "))
print("Multiplication Table of", n)
for i in range(1, 11):
  result = n * i
  print(f"{n} x {i} = {result}")
