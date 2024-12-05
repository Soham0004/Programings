from random import shuffle
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
card_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
deck = []
for suit in suits:
  for value in card_values.keys():
    deck.append({"suit": suit, "value": card_values[value]})
shuffle(deck)
hand = deck[:3]
is_flush = all(card["suit"] == hand[0]["suit"] for card in hand)
value_counts = {card["value"]: 0 for card in hand}
for card in hand:
  value_counts[card["value"]] += 1
is_three_of_a_kind = any(count == 3 for count in value_counts.values())
is_pair = any(count == 2 for count in value_counts.values()) and not is_three_of_a_kind
sorted_hand = sorted(hand, key=lambda card: card["value"])
is_straight = (
    (sorted_hand[0]["value"] + 2 == sorted_hand[1]["value"] and sorted_hand[1]["value"] + 1 == sorted_hand[2]["value"])
)
if not is_straight and hand[0]["value"] == 2:
  is_straight = (
      hand[1]["value"] == 3 and hand[2]["value"] == 14
  )
print(f"Hand: {hand}")
print(f"Is flush: {is_flush}")
print(f"Is three-of-a-kind: {is_three_of_a_kind}")
print(f"Is pair: {is_pair}")
print(f"Is straight: {is_straight}")
