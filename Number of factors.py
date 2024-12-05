def number_of_factors():
  n = int(input("Enter an integer: "))
  factor_count = 0
  for i in range(1, n + 1):
    if n % i == 0:
      factor_count += 1
  print(f"The number of factors of {n} is: {factor_count}")
number_of_factors()
