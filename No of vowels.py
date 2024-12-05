text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
  if char in vowels:
    vowel_count += 1
print("The string '" + text + "' contains " + str(vowel_count) + " vowels.")
