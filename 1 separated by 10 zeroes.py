def generate_ones_with_zeroes():
  ones_list = [1]
  zeroes_count = 1
  while True:
    ones_list.extend([0] * zeroes_count)
    ones_list.append(1)
    zeroes_count += 1
    if zeroes_count == 11:
      break
  return ones_list
ones_with_zeroes = generate_ones_with_zeroes()
print(ones_with_zeroes)
