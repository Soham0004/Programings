p = int(input("Enter the divisor (p): "))
q = int(input("Enter the non-divisor (q): "))
start = int(input("Enter the starting point of the range: "))
end = int(input("Enter the ending point of the range: "))
if p <= 0 or q <= 0 :
  print("Invalid input! Both p and q must be positive numbers, with q greater than p.")
  exit()
divisible_numbers = []
for number in range(start, end + 1):
  if number % p == 0 and number % q != 0:
    divisible_numbers.append(number)
if divisible_numbers:
  print(f"Whole numbers divisible by {p} but not by {q} within the range {start}-{end}:")
  print(*divisible_numbers, sep=", ")
else:
  print(f"No whole numbers within the range {start}-{end} are divisible by {p} but not by {q}.")
