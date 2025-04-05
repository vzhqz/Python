import random

def displayChoices(user, computer):
    print(f"\nYou: {user}")
    print(f"Computer: {computer}\n")

def displayWins(user, computer):
    print(f"\nYou won {user} times")
    print(f"Computer won {computer} times")
    if(user > computer):
        print("\nYou won!\n")
    elif(user < computer):
        print("\nComputer won.\n")
    else:
        print("Draw.")

user_wins = 0
computer_wins = 0
choices = ["rock", "paper", "scissors"]
win_cases = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]

while True:
    user_choice = input("Please enter Rock, Paper or Scissors, q to quit: ").lower()

    if user_choice == "q":
        displayWins(user_wins, computer_wins)
        break

    elif user_choice not in choices:
        print("\nInvalid choice. Please type Rock, Paper or Scissors.\n")
        continue

    computer_choice = random.choice(choices)
    displayChoices(user_choice, computer_choice)

    if user_choice == computer_choice:
        print("\nDRAW!\n")

    elif (user_choice, computer_choice) in win_cases:
        print("You won!\n")
        user_wins += 1

    else:
        print("You lost.\n")
        computer_wins += 1
