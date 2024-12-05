def root():
 number = float(input("Enter a number: "))
 n = int(input("Enter the root (optional, default is 2): ") or 2)
 result = number ** (1 / n)
 print(f"The {n}th root of {number} is: {result}")
root()
