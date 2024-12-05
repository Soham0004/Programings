def find_matching_strings(pattern, strings):
  pattern_dict = {}
  for i, char in enumerate(pattern):
    if char != "*":
      pattern_dict[i] = char
  matching_strings = []
  for string in strings:
    if all(string[i] == pattern_dict.get(i, string[i]) for i in range(len(string))):
      matching_strings.append(string)
  return matching_strings
L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']
user_pattern = input("Enter the pattern with asterisks: ")
matching_strings = find_matching_strings(user_pattern, L)
print("Matching strings:", matching_strings)
