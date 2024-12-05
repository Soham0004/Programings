conversions = [
    ["inches", 1, 0.0277778, 0.0000254, 25.4, 2.54, 0.0254 * 100, 0.0000254 * 1000],
    ["yards", 36, 1, 0.000568182, 914.4, 91.44, 0.9144 * 100, 0.0009144 * 1000],
    ["miles", 63360, 1760, 1, 1609344, 160934.4, 1609.344 * 100, 1.609344 * 1000],
    ["millimeters", 0.0393701, 0.00109361, 0.000000621371, 1, 0.1, 0.001, 0.000001],
    ["centimeters", 0.393701, 0.0109361, 0.00000621371, 10, 1, 0.01, 0.00001],
    ["meters", 39.3701 * 100, 1.09361 * 100, 0.000621371 * 100, 1000, 100, 1, 0.001],
    ["kilometers", 39370.1 * 1000, 1093.61 * 1000, 0.621371 * 1000, 1000000, 100000, 1000, 1]
]
units = ["inches", "yards", "miles", "millimeters", "centimeters", "meters", "kilometers"]
def convert_length():
    while True:
        try:
            original_length = float(input("Enter a length: "))
            original_unit = input("Enter the unit of the length ({}): ".format(", ".join(units)))
            target_unit = input("Enter the unit you want to convert to ({}): ".format(", ".join(units)))
            if original_unit not in units or target_unit not in units:
                raise ValueError("Invalid unit")
            original_index = units.index(original_unit)
            target_index = units.index(target_unit)
            conversion_factor = conversions[original_index][target_index]
            converted_length = original_length * conversion_factor
            print(f"{original_length} {original_unit} is equal to {converted_length:.4f} {target_unit}")
        except ValueError as e:
            print(e)
convert_length()
