def is_prime(num):
 if num <= 1:
   return False
 elif num <= 3:
   return True
 elif num % 2 == 0 or num % 3 == 0:
   return False
 i = 5
 while i * i <= num:
   if num % i == 0 or num % (i + 2) == 0:
     return False
   i += 6
 return True
def primes(n=100, start=2):
 prime_list = []
 num = start
 while len(prime_list) < n:
   if is_prime(num):
     prime_list.append(num)
   num += 1
 print(f"The first {n} primes greater than or equal to {start} are: {prime_list}")
num_primes = int(input("Enter the number of primes to generate (default is 100): ") or 100)
starting_num = int(input("Enter the starting number (default is 2): ") or 2)
primes(num_primes, starting_num)
