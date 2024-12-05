def binary_search(words, target):
    low, high = 0, len(words) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_word = words[mid]
        if mid_word == target:
            return True
        elif mid_word < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
word_input = input("Enter a sorted list of words separated by spaces: ")
WORDS = word_input.split()
target_word = input("Enter the word to search: ")
result = binary_search(sorted(WORDS), target_word)
if result:
    print(f"{target_word} is in the list.")
else:
    print(f"{target_word} is not in the list.")
