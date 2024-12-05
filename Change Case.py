def change_case():
  text = input("Enter a string: ")
  new_text = ""
  for char in text:
    if char.isupper():
      new_text += char.lower()
    else:
      new_text += char.upper()
  print(f"Changed-case string: {new_text}")
change_case()
