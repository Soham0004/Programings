def is_divisible():
  num = int(input("Enter a number: "))
  divisor = int(input("Enter the divisor: "))
  if num % divisor == 0:
    print(f"{num} is divisible by {divisor}.")
  else:
    print(f"{num} is not divisible by {divisor}.")
is_divisible()
