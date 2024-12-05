def power(a, b):
  """Calculates a^b recursively."""

  if b == 0:
    return 1
  else:
    return a * power(a, b - 1)

def square_root(x, epsilon=1e-6):
  """Calculates the square root of x recursively using Newton's method."""

  guess = x / 2.0
  while abs(guess * guess - x) >= epsilon:
    guess = (guess + x / guess) / 2.0
  return guess

def complex_square_root(z):
  """Calculates the square root of a complex number recursively."""

  if z == 0:
    return 0
  else:
    r = abs(z)
    theta = z.real / r
    sqrt_r = square_root(r)
    sqrt_theta = theta / 2
    return sqrt_r * (math.cos(sqrt_theta) + 1j * math.sin(sqrt_theta))

def sum_of_digits(n):
  """Calculates the sum of digits of n recursively."""

  if n == 0:
    return 0
  else:
    return n % 10 + sum_of_digits(n // 10)

def num_digits(n):
  """Calculates the number of digits in n recursively."""

  if n == 0:
    return 0
  else:
    return 1 + num_digits(n // 10)

def sum_of_power_digits(n):
  """Calculates the sum of digits of n, each raised to the power of the number of digits, recursively."""

  num_digits = num_digits(n)
  def helper(n, power):
    if n == 0:
      return 0
    else:
      return (n % 10) ** power + helper(n // 10, power)
  return helper(n, num_digits)

def sum_series(x, n):
  """Calculates the sum of the series x + (x^2)/2 + (x^3)/3 + ... up to n terms recursively."""

  if n == 0:
    return 0
  else:
    return x + (x ** 2) / n + sum_series(x, n - 1)

def sum_even_series(n):
  """Calculates the sum of even numbers from 2 to n recursively."""

  if n <= 0:
    return 0
  else:
    return n * (n + 1) // 2 + sum_even_series(n - 2)

def fibonacci(n):
  """Calculates the nth term of the Fibonacci series."""

  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

def is_palindrome(s):
  """Checks if a string is a palindrome recursively."""

  def helper(left, right):
    if left >= right:
      return True
    elif s[left] != s[right]:
      return False
    else:
      return helper(left + 1, right - 1)

  return helper(0, len(s) - 1)
