def decimal_to_base(number, base):
    if not 2 <= base <= 16:
        raise ValueError("Base must be between 2 and 16")
    if number < 0:
        raise ValueError("Number must be non-negative")
    digits = "0123456789ABCDEF"
    result = ""
    while number > 0:
        remainder = number % base
        result += digits[remainder]
        number //= base
    return result[::-1]
number = int(input("Enter a decimal number: "))
base = int(input("Enter the base to convert to (2-16): "))
converted_number = decimal_to_base(number, base)
print(f"The number {number} in base {base} is: {converted_number}")
