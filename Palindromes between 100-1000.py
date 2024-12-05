palindromes = [num for num in range(100, 1001) if str(num) == str(num)[::-1]]
print("List of palindromic numbers between 100 and 1000:", palindromes)
