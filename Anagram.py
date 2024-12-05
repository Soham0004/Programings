import random
def random_anagram(word):
 """Generates a random anagram of a word."""
 chars = list(word)
 random.shuffle(chars)
 anagram = "".join(chars)
 return anagram
word = input("Enter a word: ")
anagram = random_anagram(word)
print("Random anagram:", anagram)
