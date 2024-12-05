import random
def random_n_digit_integer(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    lower_bound = 10 ** (n - 1)
    upper_bound = 10 ** n - 1
    return random.randint(lower_bound, upper_bound)
n = int(input("Enter the number of digits (n): "))
random_number = random_n_digit_integer(n)
print(f"Random {n}-digit integer: {random_number}")
