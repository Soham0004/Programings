def abbreviate_string(text):
  """Abbreviates a string by taking the first letter of each word, excluding articles and prepositions."""
  words = text.split()
  abbreviation = ""
  articles_and_prepositions = {"the", "a", "an", "of", "in", "for", "on", "to", "by", "with"}
  for word in words:
    if word.lower() not in articles_and_prepositions:
      abbreviation += word[0].upper()
  return abbreviation
text = input("Enter the string to abbreviate: ")
abbreviation = abbreviate_string(text)
print("Abbreviated string:", abbreviation)
