CP = float(input("Enter the cost price: "))
SP = float(input("Enter the selling price: "))
if SP > CP:
    profit = SP - CP
    print("Profit:", profit)
elif SP < CP:
    loss = CP - SP
    print("Loss:", loss)
else:
    print("No profit, no loss")
