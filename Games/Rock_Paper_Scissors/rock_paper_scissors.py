import os 
import time
import random 

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def typing(message, delay=0.05):
    """Print a message with a typing effect."""
    for letter in message:
        print(letter, end='', flush=True)
        time.sleep(delay)
    print()

def hold_screen(message="Press Enter to continue..."):
    """Hold the screen until the user presses Enter."""
    input(message)

def get_user_choice():
    """Get and validate the user's choice."""
    while True:
        typing("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
        user_choice = int(input())
        if user_choice in [0, 1, 2]:
            return user_choice
        else:
            typing("Invalid choice. Please enter 0, 1, or 2.")

def get_user_name():
    """Prompt the user for their name."""
    while True:
        typing("What's your name?")
        name = input().strip().title()
        if name:
            return name
        else:
            typing("Name cannot be empty. Please enter a valid name.")

def display_choices(user_choice, computer_choice, icons):
    """Display the choices of the user and computer."""
    typing(f"You chose:{user_choice}")
    print(icons[user_choice])
    typing(f"Computer chose:{computer_choice}")
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

def play_game():
    """ Rock, Paper , Scissors Game """
    icons = ['''    
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
    ''' , 
    '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''']

    clear_screen()
    typing("Welcome to 🪨 Rock, 📄 Paper, ✂ Scissors!", delay=0.07)
    name = get_user_name()

    user_score = 0
    computer_score = 0

    while True:
        clear_screen()
        computer_choice = random.randint(0, 2)
        user_choice = get_user_choice()

        display_choices(user_choice, computer_choice, icons)

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            typing("It's a tie!")
        elif result == "user":
            typing(f"{name}, you won this round!")
            user_score += 1
        else:
            typing("Computer won this round!")
            computer_score += 1

        typing("Do you want to play again? (yes/no)")
        play_again = input().strip().lower()
        if play_again not in ["yes", "y"]:
            typing("Thanks for playing!")
            typing(f"Here are the Final Scores: {name} {user_score} - {computer_score} Computer")
            typing("See you next time!")
            break

# Run the game
play_game()
