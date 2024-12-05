def convert_to_words(number):
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = number // 1000
    remainder = number % 1000
    hundreds = remainder // 100
    remainder %= 100
    tens_part = remainder // 10
    units_part = remainder % 10
    words = ""
    if thousands:
        words += units[thousands] + " Thousand"
    if hundreds:
        words += " " if words else ""
        words += units[hundreds] + " Hundred"
    if tens_part:
        if tens_part == 1 and units_part:
            words += " " if words else ""
            words += teens[units_part]
        else:
            words += " " if words else ""
            words += tens[tens_part]
            if units_part:
                words += "-" + units[units_part]
    elif units_part:
        words += " " if words else ""
        words += units[units_part]
    return words.strip()
number = int(input("Enter an integer: "))
result = convert_to_words(number)
print(f"In words: {result}")
