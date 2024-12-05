def count_words(sentence):
  words = sentence.split()
  word_count = len(words)
  return word_count
sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
print(f"The number of words in the sentence is: {word_count}")
