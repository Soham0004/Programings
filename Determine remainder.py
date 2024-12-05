def find_remainder(dividend, divisor):
    return dividend % divisor
num1 = int(input("Enter the dividend: "))
num2 = int(input("Enter the divisor: "))
remainder = find_remainder(num1, num2)
print("Remainder:", remainder)
