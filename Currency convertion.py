def convert_rupees(rupees):
    pound_rate = 119.00
    dollar_rate = 88.01
    euro_rate = 103.32
    pounds = rupees / pound_rate
    dollars = rupees / dollar_rate
    euros = rupees / euro_rate
    return pounds, dollars, euros
rupees = float(input("Enter the amount in rupees: "))
pounds, dollars, euros = convert_rupees(rupees)
print("Converted amounts:")
print("Pounds:", pounds)
print("Dollars:", dollars)
print("Euros:", euros)
