def censor_text(text, curse_words):
 """Censors curse words in a text with asterisks."""
 censored_text = ""
 for word in text.split():
   if word.lower() in curse_words:
     censored_text += "*" * len(word) + " "
   else:
     censored_text += word + " "
 return censored_text
curse_words = ["darn", "dang", "freakin", "heck", "shoot"]
text = input("Enter some text: ")
censored_text = censor_text(text, curse_words)
print(censored_text)
