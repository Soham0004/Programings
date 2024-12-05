from random import shuffle
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
card_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
deck = []
for suit in suits:
  for value in card_values.keys():
    deck.append({"suit": suit, "value": card_values[value]})
shuffle(deck)
player1_cards = deck[:3]
player2_cards = deck[3:6]
player1_highest_value = max(card["value"] for card in player1_cards)
player2_highest_value = max(card["value"] for card in player2_cards)
if player1_highest_value > player2_highest_value:
  winner = "Player 1"
elif player1_highest_value < player2_highest_value:
  winner = "Player 2"
else:
  player1_second_highest_value = sorted(card["value"] for card in player1_cards)[-2]
  player2_second_highest_value = sorted(card["value"] for card in player2_cards)[-2]
  if player1_second_highest_value > player2_second_highest_value:
    winner = "Player 1"
  elif player1_second_highest_value < player2_second_highest_value:
    winner = "Player 2"
  else:
    player1_third_highest_value = sorted(card["value"] for card in player1_cards)[-3]
    player2_third_highest_value = sorted(card["value"] for card in player2_cards)[-3]
    if player1_third_highest_value > player2_third_highest_value:
      winner = "Player 1"
    elif player1_third_highest_value < player2_third_highest_value:
      winner = "Player 2"
    else:
      winner = "Draw"
print(f"Player 1 cards: {player1_cards}")
print(f"Player 2 cards: {player2_cards}")
print(f"Winner: {winner}")
