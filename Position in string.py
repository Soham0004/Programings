def find_all():
  text = input("Enter a string: ")
  char = input("Enter a character to find: ")
  indices = []
  start = 0
  while True:
    index = text.find(char, start)
    if index == -1:
      break
    indices.append(index)
    start = index + 1
  print(f"All indices of '{char}' in '{text}': {indices}")
find_all()
