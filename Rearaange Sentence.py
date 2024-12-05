import random
def rearrange_words(sentence):
  words = sentence.split()
  random.shuffle(words)
  return " ".join(words)
def rearrange_words_with_punctuation(sentence):
  words = sentence.split()
  first_word = words[0]
  last_word = words.pop()
  random.shuffle(words)
  words[0] = words[0].capitalize()
  if first_word != words[0]:
    words[words.index(first_word)] = first_word.lower()
  return " ".join(words + [last_word])
sentence = input("Enter a sentence: ")
rearranged_sentence_a = rearrange_words(sentence)
print("Rearranged sentence (a):", rearranged_sentence_a)
rearranged_sentence_b = rearrange_words_with_punctuation(sentence)
print("Rearranged sentence (b):", rearranged_sentence_b)
