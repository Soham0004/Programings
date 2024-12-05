fixed_charge = 75
charge_per_call_75 = 0.75
charge_per_call_90 = 0.65
charge_per_call_rest = 0.55

def calculate_monthly_bill(call_details):
    total_calls = 0
    total_charge = 0
    if call_details['calls'] <= 75:
        total_calls = call_details['calls']
        total_charge = fixed_charge
    else:
        total_calls = 75
        total_charge = fixed_charge
    remaining_calls = call_details['calls'] - total_calls
    if remaining_calls > 0:
        if remaining_calls <= 75:
            total_calls += remaining_calls
            total_charge += remaining_calls * charge_per_call_75
        else:
            total_calls += 75
            total_charge += 75 * charge_per_call_75
            remaining_calls -= 75
    if remaining_calls > 0:
        if remaining_calls <= 90:
            total_calls += remaining_calls
            total_charge += remaining_calls * charge_per_call_90
        else:
            total_calls += 90
            total_charge += 90 * charge_per_call_90
            remaining_calls -= 90
    if remaining_calls > 0:
        total_calls += remaining_calls
        total_charge += remaining_calls * charge_per_call_rest
    return total_charge
call_details = {
    "calls": int(input("Enter the number of calls: "))
}
monthly_bill = calculate_monthly_bill(call_details)
print("Monthly bill:", monthly_bill)
