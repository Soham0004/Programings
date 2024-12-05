def first_diff(str1, str2):
    min_len = min(len(str1), len(str2))
    for i in range(min_len):
        if str1[i] != str2[i]:
            return i
    if len(str1) != len(str2):
        return min_len
    else:
        return -1
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
result = first_diff(string1, string2)
if result == -1:
    print("-1")
else:
    print(f"The first difference is at index {result}.")
