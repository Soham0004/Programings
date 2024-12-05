def find_unique_digit_number(numbers):
    for i in range(4):
        digit_positions = [str(num)[i] for num in numbers]
        if len(set(digit_positions)) == 1:
            return int(digit_positions[0])
    return None
if __name__ == "__main__":
    numbers = [1265, 12171, 23257, 34548, 45970, 56236, 67324, 78084, 89872, 99414]
    unique_digit = find_unique_digit_number(numbers)
    if unique_digit is not None:
        print(f"The unique digit in the same position is: {unique_digit}")
    else:
        print("No such five-digit number found.")
