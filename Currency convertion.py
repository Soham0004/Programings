def convert_rupees(rupees):
    pound_rate = 98.73
    dollar_rate = 82.36
    euro_rate = 88.23
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
