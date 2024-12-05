def currency_breakdown():
    # Get the amount from the user
    amount = int(input("Enter the amount: "))

    # Initialize note counts
    two_thousand_notes = 0
    five_hundred_notes = 0
    two_hundred_notes = 0
    one_hundred_notes = 0

    # Break down the amount into denominations
    while amount >= 2000:
        two_thousand_notes += 1
        amount -= 2000

    while amount >= 500:
        five_hundred_notes += 1
        amount -= 500

    while amount >= 200:
        two_hundred_notes += 1
        amount -= 200

    while amount >= 100:
        one_hundred_notes += 1
        amount -= 100

    # Display the note counts
    print("2000-rupee notes:", two_thousand_notes)
    print("500-rupee notes:", five_hundred_notes)
    print("200-rupee notes:", two_hundred_notes)
    print("100-rupee notes:", one_hundred_notes)


# Call the currency_breakdown function
currency_breakdown()
