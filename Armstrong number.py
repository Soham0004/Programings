def is_armstrong_number():
 num = int(input("Enter a number: "))
 original_num = num
 sum = 0
 power = len(str(num))
 while num > 0:
   digit = num % 10
   sum += digit ** power
   num //= 10
 if sum == original_num:
   print(f"{original_num} is an Armstrong number.")
 else:
   print(f"{original_num} is not an Armstrong number.")
is_armstrong_number()
