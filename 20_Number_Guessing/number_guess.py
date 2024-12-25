from .logo import logo
from common_functions import typing, hold_screen, clear_screen, get_input
import random
    
   
def level(input):
    """Set the number of attempts based on difficulty level."""
    if input == 'easy':
        attempts = 10
    else:
        attempts = 5
    return attempts

def random_number():
    """Generates a Random Number from 1 to 100."""
    return random.randint(1,100)


def logic(random_digit, guess):
    """Check if the guessed number is correct, too high, or too low."""
    if guess == random_digit:
        return "You Guessed it Right!"
    elif guess > random_digit:
        return "Too High!"
    else:  # Only possibility left is guess < random_digit
        return "Too Low!"

clear_screen()
print(logo)
typing("Welcome to the Number Guessing Game!\n")
typing("I'm thinking of a number between 1 and 100.\n")

random_digit = random_number()

choice = get_input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts = level(choice)
typing(f"You have {attempts} attempts remaining to guess the number.\n")
while attempts > 0:
    guess = get_input("Make a guess: ",is_int=True)
    message = logic(random_digit, guess)
    print(message)
    if message == "You Guessed it Right!":
         break
    attempts -= 1
    typing(f"You have {attempts} attempts remaining to guess the number.\n")

typing(f"Correct Answer : {random_digit}\n")
typing("Thanks for playing!\n")
