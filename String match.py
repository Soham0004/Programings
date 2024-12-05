def matches(str1, str2):
  count = 0
  for i in range(min(len(str1), len(str2))):
    if str1[i] == str2[i]:
      count += 1
  return count
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
match_count = matches(str1, str2)
print(f"The number of matches between '{str1}' and '{str2}' is: {match_count}")
