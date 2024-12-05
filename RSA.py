def is_prime(num):
    """Checks if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    """Calculates the greatest common divisor using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Calculates the modular inverse using the extended Euclidean algorithm."""
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t
    if x1 < 0:
        x1 += m0
    return x1

def generate_keys(p, q):
    """Generates RSA public and private keys."""
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that 1 < e < phi and gcd(e, phi) = 1
    e = 65537  # Common value for e
    while gcd(e, phi) != 1:
        e += 2  # Ensure e is odd for efficiency

    d = mod_inverse(e, phi)
    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key

# Get prime numbers from the user
p = int(input("Enter a large prime number (p): "))
q = int(input("Enter another large prime number (q): "))

# Generate keys
public_key, private_key = generate_keys(p, q)

# Display the keys
print("\nPublic Key:", public_key)
print("Private Key:", private_key)
