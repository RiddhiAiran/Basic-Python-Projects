from common_functions import typing, hold_screen, clear_screen, get_input
import random 
import time 

def get_range():
    """Prompt the user for a valid range."""
    while True:
        typing("Enter the lower bound of the range:")
        lower = int(input())
        typing("Enter the upper bound of the range:")
        upper = int(input())
        if lower < upper:
            return lower, upper
        else:
            typing("Invalid range. The lower bound must be less than the upper bound.")

def generate_random_number(lower, upper):
    """Random Number Generator program."""
    return random.randint(lower, upper)

def random_number_generator():
    """Random Number Generator program."""
    clear_screen()
    typing("Welcome to the Random Number Generator!", delay=0.07)
    hold_screen()
    while True:
        clear_screen()
        lower, upper = get_range()
        random_number = generate_random_number(lower, upper)
        typing(f"Generating a random number between {lower} and {upper}...")
        time.sleep(1)
        typing(f"Your random number is: {random_number}")
        typing("Do you want to generate another random number? (yes/no)")
        play_again = input().strip().lower()
        if play_again not in ["yes","y"]:
            typing("Thanks for using the Random Number Generator! Goodbye!")
            break
    
# Run the random number generator
random_number_generator()
