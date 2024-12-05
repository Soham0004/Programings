def calculate_parking_charge(parking_duration):
    if parking_duration <= 8.5:
        charge = 55
    else:
        remaining_duration = parking_duration - 8.5
        two_hour_intervals = int(remaining_duration // 2)
        charge = 55 + two_hour_intervals * 13.75
        remaining_minutes = remaining_duration % 2 * 60
        if remaining_minutes > 0:
            charge += remaining_minutes * 0.055
    return charge
parking_duration = float(input("Enter the parking duration in hours: "))
parking_charge = calculate_parking_charge(parking_duration)
print("Parking charge:", parking_charge)
