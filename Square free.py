def is_square_free(n):
  if n <= 1:
    return True
  i = 2
  while i * i <= n:
    if n % (i * i) == 0:
      return False
    i += 1
  return True
number = int(input("Enter an integer to check if it's square-free: "))
if is_square_free(number):
  print(f"{number} is square-free.")
else:
  print(f"{number} is not square-free.")
