def convert_length(length, from_unit, to_unit):
    conversion_factors = {
        "inches": {"inches": 1, "yards": 1 / 36, "miles": 1 / 63360, "millimeters": 25.4, "centimeters": 2.54, "meters": 0.0254, "kilometers": 0.0000254},
        "yards": {"inches": 36, "yards": 1, "miles": 1 / 1760, "millimeters": 914.4, "centimeters": 91.44, "meters": 0.9144, "kilometers": 0.0009144},
        "miles": {"inches": 63360, "yards": 1760, "miles": 1, "millimeters": 1609344, "centimeters": 160934.4, "meters": 1609.344, "kilometers": 1.609344},
        "millimeters": {"inches": 0.03937, "yards": 0.00109361, "miles": 6.2137e-7, "millimeters": 1, "centimeters": 0.1, "meters": 0.001, "kilometers": 1e-6},
        "centimeters": {"inches": 0.393701, "yards": 0.0109361, "miles": 6.2137e-6, "millimeters": 10, "centimeters": 1, "meters": 0.01, "kilometers": 1e-5},
        "meters": {"inches": 39.3701, "yards": 1.09361, "miles": 6.2137e-4, "millimeters": 1000, "centimeters": 100, "meters": 1, "kilometers": 0.001},
        "kilometers": {"inches": 39370.1, "yards": 1093.61, "miles": 0.621371, "millimeters": 1e6, "centimeters": 1e5, "meters": 1000, "kilometers": 1}
    }
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return "Invalid units"
    result = length * conversion_factors[from_unit][to_unit]
    return result
if __name__ == "__main__":
    length = float(input("Enter the length: "))
    from_unit = input("Enter the current unit (e.g., inches, yards, miles, millimeters, centimeters, meters, kilometers): ").lower()
    to_unit = input("Enter the unit you want to convert to: ").lower()
    converted_length = convert_length(length, from_unit, to_unit)
    print(f"{length} {from_unit} is equal to {converted_length} {to_unit}")
