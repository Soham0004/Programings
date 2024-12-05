alphabet = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o','p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x','y', 'z']
cipher = ''
text = input("Enter the word: ").lower()
key = input("Enter the key: ").lower()
for i in range(len(text)):
    cipher += alphabet[(alphabet.index(text[i])+alphabet.index(key[i]))%26]
print("The cipher text: ", cipher)
