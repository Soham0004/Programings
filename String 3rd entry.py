sentence = input("Enter a sentence: ")
words = sentence.split()
if len(words) >= 3:
  third_word = words[2]
  print("Third word:", third_word)
else:
  print("Sentence has fewer than three words.")
print("Every third word:")
for i in range(2, len(words), 3):
  print(words[i])
