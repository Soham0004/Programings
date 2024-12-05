def calculate_festival_bonus(basic_pay, designation):
    if designation == "Manager":
        if basic_pay < 40000:
            bonus = max(2500, 0.12 * basic_pay)
        else:
            bonus = min(7500, 0.16 * basic_pay)
    elif designation == "Officer":
        bonus = max(2500, min(5000, 0.14 * basic_pay))
    else:
        bonus = 0.089 * basic_pay
    return bonus
basic_pay = float(input("Enter the basic pay: "))
designation = input("Enter the designation (Manager, Officer, other): ")
festival_bonus = calculate_festival_bonus(basic_pay, designation)
print("Festival bonus:", festival_bonus)
