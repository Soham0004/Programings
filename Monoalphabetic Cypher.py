def monoalphabetic_cipher(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_map = {}

    # Create mapping
    for i in range(len(alphabet)):
        shifted_index = (i + key) % len(alphabet)
        cipher_map[alphabet[i]] = alphabet[shifted_index]

    ciphertext = ""
    for char in plaintext.lower():
        if char in cipher_map:
            ciphertext += cipher_map[char]
        else:
            ciphertext += char
    return ciphertext

# Input with error handling
plaintext = input("Enter the plaintext: ")
try:
    key = int(input("Enter the key value (0-25): "))
    if not 0 <= key <= 25:
        print("Key must be between 0 and 25.")
    else:
        ciphertext = monoalphabetic_cipher(plaintext, key)
        print("Ciphertext:", ciphertext)
except ValueError:
    print("Please enter a valid integer for key.")
