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
            typing("Invalid range. The lower bound must be less than the upper bound.\n")

def generate_random_number(lower, upper):
    """Random Number Generator program."""
    return random.randint(lower, upper)

def random_number_generator():
    """Random Number Generator program."""
    clear_screen()
    typing("Welcome to the Random Number Generator!\n")
    lower, upper = get_range()
    random_number = generate_random_number(lower, upper)
    typing(f"Generating a random number between {lower} and {upper}...\n")
    time.sleep(1)
    typing(f"Your random number is: {random_number}\n")
    hold_screen()

def main():
    """ Main Function to run the Generator """
    while True:
        
        clear_screen()
        play_again = get_input("Do you want to generate another random number? (yes/no) : ").lower()
        if play_again == "yes":
            hold_screen()
            random_number_generator()
        else:
            typing("Thanks for Coming, Goodbye!\n")
            break
    
if __name__ == '__main__':
    main()
