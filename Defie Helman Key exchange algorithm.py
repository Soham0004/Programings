import random
def is_prime(num):
    """Checks if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def primitive_root(modulo):
    """Finds a primitive root modulo a prime number."""
    required_set = set(range(1, modulo))
    for root in range(1, modulo):
        actual_set = set(pow(root, powers, modulo) for powers in range(1, modulo))
        if required_set == actual_set:
            return root
    return None
def diffie_hellman():
    """Implements the Diffie-Hellman key exchange algorithm."""
    p = int(input("Enter a large prime number (p): "))
    while not is_prime(p):
        print("Invalid prime number. Please enter a valid prime number.")
        p = int(input("Enter a large prime number (p): "))
    g = int(input("Enter a primitive root modulo p: "))
    while primitive_root(p) != g:
        print("Invalid primitive root. Please enter a valid primitive root modulo p.")
        g = int(input("Enter a primitive root modulo p: "))
    a = int(input("Enter User A's private key (a): "))
    A = pow(g, a, p)
    b = int(input("Enter User B's private key (b): "))
    B = pow(g, b, p)
    key_A = pow(B, a, p)
    key_B = pow(A, b, p)
    print("\nShared Secret Key (Key at Sender):", key_A)
    print("Shared Secret Key (Key at Receiver):", key_B)
if __name__ == "__main__":
    diffie_hellman()
