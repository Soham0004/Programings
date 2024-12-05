def find_factors(num):
  """Returns a list of factors of a given integer."""
  factors = []
  for i in range(1, num + 1):
    if num % i == 0:
      factors.append(i)
  return factors
num = int(input("Enter an integer: "))
factors = find_factors(num)
print("Factors of", num, ":", factors)
