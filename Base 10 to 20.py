def base20(number):
  digits = "0123456789ABCDEFGHIJ"
  result = ""
  while number > 0:
    remainder = number % 20
    result += digits[remainder]
    number //= 20
  return result[::-1]
base10_number = int(input("Enter a base 10 number: "))
base20_representation = base20(base10_number)
print(f"The base 20 representation of {base10_number} is: {base20_representation}")
