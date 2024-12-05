word = input("Enter a word: ")
clean_word = "".join(char.lower() for char in word if char.isalnum())
reversed_word = clean_word[::-1]
if clean_word == reversed_word:
  print(f"'{word}' is a palindrome!")
else:
  print(f"'{word}' is not a palindrome.")
