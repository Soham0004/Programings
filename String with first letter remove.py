strings_input = input("Enter a list of strings separated by spaces: ")
strings = strings_input.split()
new_strings = [string[1:] for string in strings]
print("New list with first characters removed:", new_strings)
