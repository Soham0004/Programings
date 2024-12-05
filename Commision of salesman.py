def calculate_commission(sales, region):
    if region == "A":
        if sales < 10000:
            commission = 0
        elif sales < 16000:
            commission = 0.065 * sales
        else:
            commission = 0.085 * sales + 1500
    else:
        if sales < 15000:
            commission = 0.065 * sales
        else:
            commission = 0.11 * sales + 4500
    return commission
sales = float(input("Enter the sales: "))
region = input("Enter the region (A or B): ")
commission = calculate_commission(sales, region)
print("Commission:", commission)
