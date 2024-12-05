binary_string = input("Enter a binary string: ")
decimal_value = 0
power = 0
for digit in binary_string[::-1]:
  if digit == '1':
    decimal_value += 2**power
print(f"The decimal equivalent of '{binary_string}' is {decimal_value}")

