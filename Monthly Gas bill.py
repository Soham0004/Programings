def calculate_gas_bill(previous_reading, current_reading, meter_rent):
    gas_consumption = current_reading - previous_reading
    therms_used = gas_consumption * 1.475
    if therms_used <= 125:
        base_charge = therms_used * 7.75
    elif therms_used <= 250:
        base_charge = 9.75 + therms_used * 9.00
    else:
        base_charge = 13.00 + therms_used * 10.50
    surcharge = 0
    if therms_used > 125:
        if therms_used <= 250:
            surcharge = base_charge * 0.0125
        else:
            surcharge = base_charge * 0.025
    total_gas_charge = base_charge + surcharge
    total_bill = total_gas_charge + meter_rent
    return total_bill
previous_reading = int(input("Enter the previous meter reading: "))
current_reading = int(input("Enter the current meter reading: "))
monthly_gas_bill = calculate_gas_bill(previous_reading, current_reading, 25)
print("Monthly gas bill:", monthly_gas_bill)
