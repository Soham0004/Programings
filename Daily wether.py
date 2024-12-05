class TemperatureAnalyzer:
    def __init__(self):
        self.temperatures = []
    def record_temperature(self, max_temp, min_temp):
        self.temperatures.append((max_temp, min_temp))
    def calculate_averages(self):
        if not self.temperatures:
            return None
        max_temps, min_temps = zip(*self.temperatures)
        avg_max_temp = sum(max_temps) / len(max_temps)
        avg_min_temp = sum(min_temps) / len(min_temps)
        return avg_max_temp, avg_min_temp
    def find_extremes(self):
        if not self.temperatures:
            return None
        hottest_day = max(self.temperatures, key=lambda x: x[0])
        coldest_day = min(self.temperatures, key=lambda x: x[1])
        hottest_temp, coldest_temp = hottest_day[0], coldest_day[1]
        hottest_day_number = self.temperatures.index(hottest_day) + 1
        coldest_day_number = self.temperatures.index(coldest_day) + 1
        return hottest_temp, coldest_temp, hottest_day_number, coldest_day_number
def main():
    analyzer = TemperatureAnalyzer()
    for day in range(1, 32):
        max_temp = float(input(f"Enter the maximum temperature for day {day}: "))
        min_temp = float(input(f"Enter the minimum temperature for day {day}: "))
        analyzer.record_temperature(max_temp, min_temp)
    averages = analyzer.calculate_averages()
    print(f"Average Maximum Temperature: {averages[0]}")
    print(f"Average Minimum Temperature: {averages[1]}")
    extremes = analyzer.find_extremes()
    print(f"Hottest Temperature: {extremes[0]}")
    print(f"Coldest Temperature: {extremes[1]}")
    print(f"Hottest Day Number: {extremes[2]}")
    print(f"Coldest Day Number: {extremes[3]}")
if __name__ == "__main__":
    main()
