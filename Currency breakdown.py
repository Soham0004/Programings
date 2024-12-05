def currency_breakdown():
    amount = int(input("Enter the amount: "))
    two_thousand_notes = 0
    five_hundred_notes = 0
    two_hundred_notes = 0
    one_hundred_notes = 0
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
    print("2000-rupee notes:", two_thousand_notes)
    print("500-rupee notes:", five_hundred_notes)
    print("200-rupee notes:", two_hundred_notes)
    print("100-rupee notes:", one_hundred_notes)
currency_breakdown()
