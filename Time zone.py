time_zones = {
    'Eastern': 0, 'Central': 1, 'Mountain': 2, 'Pacific': 3
}
def convert_time(original_time, starting_zone, ending_zone):
    hours, minutes = map(int, original_time[:-2].split(':'))
    am_pm = original_time[-2:]
    time_difference = time_zones[ending_zone] - time_zones[starting_zone]
    hours = (hours + time_difference) % 12
    if am_pm.lower() == 'pm':
        hours += 12
    result_time = f"{hours:02d}:{minutes:02d}{'am' if hours < 12 else 'pm'}"
    return result_time
def main():
    original_time = input("Enter the time (e.g., 3:48pm): ")
    starting_zone = input("Enter the starting time zone (Eastern, Central, Mountain, Pacific): ")
    ending_zone = input("Enter the ending time zone (Eastern, Central, Mountain, Pacific): ")
    if starting_zone not in time_zones or ending_zone not in time_zones:
        print("Invalid time zone.")
        return
    converted_time = convert_time(original_time, starting_zone, ending_zone)
    print(f"The converted time is: {converted_time}")
if __name__ == "__main__":
    main()
