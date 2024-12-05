def feet_to_inches(feet):
    return feet * 12
def feet_to_yards(feet):
    return feet / 3.0
def feet_to_miles(feet):
    return feet / 5280.0
def feet_to_millimeters(feet):
    return feet * 304.8
def feet_to_centimeters(feet):
    return feet * 30.48
def feet_to_meters(feet):
    return feet * 0.3048
def feet_to_kilometers(feet):
    return feet * 0.0003048
def main():
    length_in_feet = float(input("Enter length in feet: "))
    conversion_options = [
        feet_to_inches,
        feet_to_yards,
        feet_to_miles,
        feet_to_millimeters,
        feet_to_centimeters,
        feet_to_meters,
        feet_to_kilometers
    ]
    print("\nConversion Options:")
    print("1. Feet to Inches")
    print("2. Feet to Yards")
    print("3. Feet to Miles")
    print("4. Feet to Millimeters")
    print("5. Feet to Centimeters")
    print("6. Feet to Meters")
    print("7. Feet to Kilometers")
    choice = int(input("Enter your choice (1-7): "))
    if 1 <= choice <= 7:
        converted_value = conversion_options[choice - 1](length_in_feet)
        print(f"{length_in_feet} feet is equal to {converted_value:.2f} in the selected unit.")
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
if __name__ == "__main__":
    main()
