from random import shuffle
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
card_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
deck = []
for suit in suits:
  for value in card_values.keys():
    deck.append({"suit": suit, "value": card_values[value]})
iterations = 100000
flush_count = 0
for _ in range(iterations):
  shuffle(deck)
  hand = deck[:5]
  flush_found = any(all(card["suit"] == suit for card in hand) for suit in suits)
  flush_count += flush_found
estimated_probability = flush_count / iterations
print(f"Estimated probability of getting a flush in a five-card hand: {estimated_probability:.4f}")
