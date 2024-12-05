products = {}
while True:
  name = input("Enter a product name (or 'Done' to finish): ")
  if name == "Done":
    break
  price = float(input("Enter the price: "))
  products[name] = price
print("\nProducts and prices:")
for name, price in products.items():
  print(f"{name}: ${price:.2f}")
while True:
  name = input("\nEnter a product name to check its price (or 'quit' to exit): ")
  if name == "quit":
    break
  if name in products:
    print(f"The price of {name} is ${products[name]:.2f}")
  else:
    print(f"Product '{name}' not found.")
