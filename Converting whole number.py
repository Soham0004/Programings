def make_positive(number):
  result = number * number
  print(f"The positive result is: {result}")
def make_negative(number):
  result = -1 * number * number
  print(f"The negative result is: {result}")
def main():
  number = int(input("Enter a whole number: "))
  if number < 0:
    make_positive(number)
  else:
    make_negative(number)
main()
