def binom():
  n = int(input("Enter the value of n: "))
  k = int(input("Enter the value of k: "))
  if k > n or k < 0:
    print("Invalid input: k must be between 0 and n.")
    return
  numerator = 1
  for i in range(1, n + 1):
    numerator *= i
  denominator = factorial(k) * factorial(n - k)
  binom_value = numerator // denominator
  print(f"The binomial coefficient ({n} choose {k}) is: {binom_value}")
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
binom()
