def matching(str1, str2):
  if len(str1) != len(str2):
    return False
  mismatch_count = 0
  for i in range(len(str1)):
    if str1[i] != str2[i]:
      mismatch_count += 1
      if mismatch_count > 1:
        return False
  return mismatch_count == 1
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
if matching(str1, str2):
  print(f"{str1} and {str2} are matching strings.")
else:
  print(f"{str1} and {str2} are not matching strings.")
