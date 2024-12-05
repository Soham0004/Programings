roman_numerals = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}
def convert_to_roman(number):
  """Converts a decimal number to a Roman numeral string."""
  roman_string = ""
  for value, symbol in roman_numerals.items():
    while number >= value:
      roman_string += symbol
      number -= value
  return roman_string
decimal_number = int(input("Enter a decimal number to convert to Roman numerals: "))
roman_number = convert_to_roman(decimal_number)
print(f"The Roman numeral equivalent of {decimal_number} is: {roman_number}")
