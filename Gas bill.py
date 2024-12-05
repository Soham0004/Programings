def calculate_gas_bill(previous_reading, current_reading, meter_rent):
    # Calculate gas consumption in cubic feet
    gas_consumption = current_reading - previous_reading

    # Convert cubic feet to therms
    therms_used = gas_consumption * 1.475

    # Calculate base gas charge
    if therms_used <= 125:
        base_charge = therms_used * 7.75
    elif therms_used <= 250:
        base_charge = 9.75 + therms_used * 9.00
    else:
        base_charge = 13.00 + therms_used * 10.50

    # Calculate surcharge if applicable
    surcharge = 0
    if therms_used > 125:
        if therms_used <= 250:
            surcharge = base_charge * 0.0125
        else:
            surcharge = base_charge * 0.025

    # Calculate total gas charge
    total_gas_charge = base_charge + surcharge

    # Calculate total bill
    total_bill = total_gas_charge + meter_rent

    return total_bill

# Prompt the user for previous and current readings
previous_reading = int(input("Enter the previous meter reading: "))
current_reading = int(input("Enter the current meter reading: "))

# Calculate monthly gas bill
monthly_gas_bill = calculate_gas_bill(previous_reading, current_reading, 25)

# Print the monthly gas bill
print("Monthly gas bill:", monthly_gas_bill)
