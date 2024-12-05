import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    
    print("Welcome to Rock, Paper, Scissors game!")
    print("Enter your choice: rock, paper, or scissors.")
    
    while True:
        # Get player's choice
        player_choice = input("Your choice: ").lower()
        
        if player_choice not in choices:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        # Computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer's choice: {computer_choice}")

        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("Congratulations! You win!")
        else:
            print("Sorry, you lose!")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    rock_paper_scissors()
