import random

min_num = 1
max_num = 100
rand_num = random.randint(min_num, max_num)
attempts = 0

while True:
    user_input = input(f"Guess a number between {min_num}-{max_num}: ")

    if not user_input.isdigit():
        print("\nInvalid number!\n")
        continue

    user_guess = int(user_input)
    attempts += 1

    if user_guess > max_num or user_guess < min_num:
        print(f"\nPlease choose a number between {min_num}-{max_num}!\n")

    elif user_guess > rand_num:
        print("\nToo big. Maybe try a smaller number?\n")
    
    elif user_guess < rand_num:
        print("\nToo small. Maybe try a bigger number?\n")
    
    else:
        print("--------------------------------------")
        print("\nYou have guessed the correct number!")
        print(f"The number was {rand_num}")
        print(f"It took you {attempts} attempts")
        break
