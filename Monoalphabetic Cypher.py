def monoalphabetic_cipher(plaintext, key):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  cipher_map = {}
  for i in range(len(alphabet)):
    shifted_index = (i + key) % len(alphabet)
    cipher_map[alphabet[i]] = alphabet[shifted_index]
  ciphertext = ""
  for char in plaintext:
    if char in alphabet:
      ciphertext += cipher_map[char]
    else:
      ciphertext += char
  return ciphertext
plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key value (0-25): "))
ciphertext = monoalphabetic_cipher(plaintext, key)
print("Ciphertext:", ciphertext)
