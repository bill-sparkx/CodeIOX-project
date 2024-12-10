import random


def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    # Validate user input
    while user_choice not in options:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()

    # Computer randomly selects a choice
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose.")


# Run the game
if __name__ == "__main__":
    rock_paper_scissors()