L_str = input("Enter a list of numbers for L separated by spaces: ")
L = [int(num) for num in L_str.split()]
M_str = input("Enter a list of numbers for M separated by spaces: ")
M = [int(num) for num in M_str.split()]
if len(L) != len(M):
  print("Error: Lists must be of the same size.")
else:
  N = [l + m for l, m in zip(L, M)]
  print("List N:", N)
