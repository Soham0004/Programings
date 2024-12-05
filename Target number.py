def closest():
  L = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
  n = int(input("Enter a target number: "))
  closest_element = None
  for element in L:
    if element <= n and (closest_element is None or element > closest_element):
      closest_element = element
  if closest_element is None:
    print("All elements in the list are larger than the target number.")
  else:
    print(f"Closest element in L to {n}: {closest_element}")
closest()
