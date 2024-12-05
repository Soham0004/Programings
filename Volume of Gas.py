def calculate_volume(initial_volume, initial_pressure, initial_temperature, final_pressure, final_temperature):
    initial_temperature += 273.15
    final_temperature += 273.15
    final_volume = (initial_volume * initial_pressure * final_temperature) / (initial_temperature * final_pressure)
    return final_volume
initial_volume = float(input("Enter the initial volume (in liters): "))
initial_pressure = float(input("Enter the initial pressure (in atmospheres): "))
initial_temperature = float(input("Enter the initial temperature (in degrees Celsius): "))
final_pressure = float(input("Enter the final pressure (in atmospheres): "))
final_temperature = float(input("Enter the final temperature (in degrees Celsius): "))
final_volume = calculate_volume(initial_volume, initial_pressure, initial_temperature, final_pressure, final_temperature)
print("Final volume (in liters):", final_volume)
