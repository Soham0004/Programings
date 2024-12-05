L = ["hello", "world", "python", "is", "awesome"]
L_without_first_chars = [word[1:] for word in L]
print("List with first characters removed:", L_without_first_chars)
string_lengths = [len(word) for word in L]
print("List of string lengths:", string_lengths)
L_filtered = [word for word in L if len(word) >= 3]
print("List of strings at least three characters long:", L_filtered)
