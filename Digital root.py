def digital_root():
  n = int(input("Enter a positive integer: "))
  while n >= 10:
    digit_sum = 0
    while n > 0:
      digit_sum += n % 10
      n //= 10
    n = digit_sum
  print(f"The digital root of the number is: {n}")
digital_root()
