text = input("Enter a string: ")
char_counts = {}
for char in text:
  if char in char_counts:
    char_counts[char] += 1
  else:
    char_counts[char] = 1
for char, count in char_counts.items():
  print(f"Character '{char}' appears {count} times.")
