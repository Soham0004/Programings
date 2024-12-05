def is_valid_substitution(text1, text2):
 if len(text1) != len(text2):
   return False
 mapping = {}
 for i in range(len(text1)):
   letter1 = text1[i].upper()
   letter2 = text2[i].upper()
   if letter1 in mapping:
     if mapping[letter1] != letter2:
       return False
   else:
     mapping[letter1] = letter2
   if letter2 in mapping.values() and mapping[letter2] != letter1:
     return False
 return True
text1 = input("Enter the original text: ")
text2 = input("Enter the potentially encoded text: ")
if is_valid_substitution(text1, text2):
 print("The second text could be an encoded version of the first text.")
else:
 print("The second text is not an encoded version of the first text.")
