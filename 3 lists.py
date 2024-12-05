list_a = list(range(60))
print("List a:", list_a)
list_b = [num**2 for num in range(1, 50)]
print("List b:", list_b)
letters = [chr(ord('a') + i) * (i + 1) for i in range(26)]
print("List c:", letters)
