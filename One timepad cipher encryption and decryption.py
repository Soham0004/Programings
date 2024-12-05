import random
def encrypt_one_time_pad(message):
  """Encrypts a message using the one-time pad cipher."""
  encrypted_message = ""
  shifts = []
  for char in message.lower():
    if char.isalpha():
      shift = random.randint(1, 26)
      shifts.append(shift)
      new_char_code = (ord(char) - ord('a') + shift) % 26 + ord('a')
      encrypted_message += chr(new_char_code)
    else:
      encrypted_message += char
  return encrypted_message, shifts
def decrypt_one_time_pad(encrypted_message, shifts):
  """Decrypts a message using the one-time pad cipher."""
  decrypted_message = ""
  shift_index = 0
  for char in encrypted_message:
    if char.isalpha():
      decrypted_char_code = (ord(char) - ord('a') - shifts[shift_index] + 26) % 26 + ord('a')
      decrypted_message += chr(decrypted_char_code)
      shift_index += 1
    else:
      decrypted_message += char
  return decrypted_message
message = input("Enter a message to encrypt: ")
encrypted_message, shifts = encrypt_one_time_pad(message)
print("Encrypted message:", encrypted_message)
decrypted_message = decrypt_one_time_pad(encrypted_message, shifts)
print("Decrypted message:", decrypted_message)
