import random
from common_functions import typing, hold_screen, clear_screen, get_input

def get_user_choice():
    """Get and validate the user's choice."""
    while True:
        user_choice = get_input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors : ", is_int=True)
        if user_choice in [0, 1, 2]:
            return user_choice
        else:
            typing("Invalid choice. Please enter 0, 1, or 2.\n")

def get_user_name():
    """Prompt the user for their name."""
    while True:
        name = get_input("What's your name? : ")
        if name:
            return name.strip()
        else:
            typing("Name cannot be empty. Please enter a valid name.")

def display_choices(user_choice, computer_choice, icons):
    """Display the choices of the user and computer."""
    typing(f"You chose:{user_choice}")
    print(icons[user_choice])
    typing(f"Computer chose: {computer_choice}")
    print(icons[computer_choice])

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "user"
    else:
        return "computer"

def play_game(name):
    """Rock, Paper, Scissors Game."""
    icons = [
        '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
        ''',
        '''
        _______
    ---'   ____)____
                ______)
                _______)
                _______)
    ---.__________)
        ''',
        '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
        '''
    ]

    user_score = 0
    computer_score = 0

    while True:
        clear_screen()
        computer_choice = random.randint(0, 2)
        user_choice = get_user_choice()

        display_choices(user_choice, computer_choice, icons)

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            typing("It's a tie!\n")
        elif result == "user":
            typing(f"{name}, you won this round!\n")
            user_score += 1
        else:
            typing("Computer won this round!\n")
            computer_score += 1

        typing(f"Scores: {name} {user_score} - {computer_score} Computer\n")

        play_again = get_input("Do you want to play another round? (yes/no) : ").lower()
        if play_again != "yes":
            break

    return user_score, computer_score


def main():
    """Main Function to run Rock Paper Scissors."""
    clear_screen()
    typing("Welcome to 🪨 Rock, 📄 Paper, ✂ Scissors!\n")
    name = get_user_name()
    hold_screen()

    while True:
        user_score, computer_score = play_game(name)
        typing(f"See you next time, {name}!\n")
        break

# Run the game
if __name__ == '__main__':
    main()
