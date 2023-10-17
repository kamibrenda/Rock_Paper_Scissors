import random

def get_user_choice():
    user_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        user_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    win_conditions = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    if win_conditions[user_choice] == computer_choice:
        return "You win!"
    return "Computer wins!"

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    if input("Play again? (yes/no): ").strip().lower() != "yes":
        break
