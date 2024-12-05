import random
def encrypt_one_time_pad(message):
  '''Encrypts a message using the one-time pad cipher.'''
  encrypted_message = ""
  for char in message:
    shift = random.randint(1, 26)
    new_char_code = (ord(char) - ord('a') + shift) % 26 + ord('a')
    encrypted_message += chr(new_char_code)
  return encrypted_message
message = input("Enter a message to encrypt: ")
encrypted_message = encrypt_one_time_pad(message)
print("Encrypted message:", encrypted_message)
