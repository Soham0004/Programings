#include <iostream>
#include <ctime>

using namespace std;

int main() {
    // Array of choices
    string choices[] = {"rock", "paper", "scissors"};

    cout << "Welcome to Rock, Paper, Scissors game!" << endl;
    cout << "Enter your choice: rock, paper, or scissors." << endl;

    while (true) {
        // Get player's choice
        string playerChoice;
        cin >> playerChoice;

        // Convert player's choice to lowercase
        for (char& c : playerChoice) {
            c = tolower(c);
        }

        bool validChoice = false;
        // Validate player's choice
        for (const string& choice : choices) {
            if (playerChoice == choice) {
                validChoice = true;
                break;
            }
        }

        if (!validChoice) {
            cout << "Invalid choice. Please enter 'rock', 'paper', or 'scissors'." << endl;
            continue;
        }

        // Seed the random number generator
        srand(time(0));

        // Generate random computer's choice
        string computerChoice = choices[rand() % 3];
        cout << "Computer's choice: " << computerChoice << endl;

        // Determine the winner
        if (playerChoice == computerChoice) {
            cout << "It's a tie!" << endl;
        } else if ((playerChoice == "rock" && computerChoice == "scissors") ||
                   (playerChoice == "paper" && computerChoice == "rock") ||
                   (playerChoice == "scissors" && computerChoice == "paper")) {
            cout << "Congratulations! You win!" << endl;
        } else {
            cout << "Sorry, you lose!" << endl;
        }

        cout << "Play again? (yes/no): ";
        string playAgain;
        cin >> playAgain;

        // Convert playAgain to lowercase
        for (char& c : playAgain) {
            c = tolower(c);
        }

        if (playAgain != "yes") {
            break;
        }
    }

    return 0;
}
