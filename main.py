import random

CHOICES = ["rock", "paper", "scissors"]

WINNING_PAIRS = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}

SHORTCUTS = {
    "r": "rock",
    "p": "paper",
    "s": "scissors",
}


def get_user_choice() -> str:
    """Prompt the user until a valid choice or exit command is provided."""
    while True:
        user_input = input("Enter rock, paper, or scissors: ").strip().lower()
        if user_input in CHOICES:
            return user_input
        if user_input in SHORTCUTS:
            return SHORTCUTS[user_input]
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")


def play_round() -> bool:
    """Play one round of Rock-Paper-Scissors and ask to play again."""
    computer_choice = random.choice(CHOICES)

    user_choice = get_user_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine outcome
    if user_choice == computer_choice:
        print("Result: It's a draw!\n")
    elif WINNING_PAIRS[user_choice] == computer_choice:
        print("Result: You won!\n")
    else:
        print("Result: You lost!\n")

    while True:
        play_again = input("Do you want to play again? (Y[yes]/E[no,exit]): ").strip().lower()
        if play_again in ("y", "Y"):
            print()
            return True
        elif play_again in ("e", "E"):
            return False
        print("Please enter 'y (yes)' or 'e (no, exit)'.")


def main() -> None:
    print("  Welcome to Rock-Paper-Scissors!   ")

    playing = True
    while playing:
        playing = play_round()

    print("\nThanks for playing! Goodbye!")


if __name__ == "__main__":
    main()
