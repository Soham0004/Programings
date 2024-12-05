def process_baby_weights():
  weights = []
  while True:
    weight_str = input("Enter a baby's weight (in kilograms) or 'done' to finish: ")
    if weight_str == "done":
      break
    try:
      weight = float(weight_str)
      weights.append(weight)
    except ValueError:
      print("Invalid input. Please enter a number or 'done'.")
  if not weights:
    print("No weights entered.")
    return
  average_weight = sum(weights) / len(weights)
  max_weight = max(weights)
  min_weight = min(weights)
  print("Results:")
  print(f"Average weight: {average_weight:.2f} kg")
  print(f"Maximum weight: {max_weight:.2f} kg")
  print(f"Minimum weight: {min_weight:.2f} kg")
process_baby_weights()
