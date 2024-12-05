text = input("Enter the string to abbreviate: ")
words = text.split()
abbreviation = ""
if len(words) == 1:
  abbreviation = text
else:
  for i in range(len(words) - 1):
    abbreviation += words[i][0].upper() + ". "
  abbreviation += words[-1]
print("Abbreviated string:", abbreviation)
