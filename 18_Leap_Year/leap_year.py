import os
import time


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def typing(message, delay=0.05):
    """Print a message with a typing effect."""
    for letter in message:
        print(letter, end='', flush=True)
        time.sleep(delay)
    

def hold_screen(message="Press Enter to continue..."):
    """Hold the screen until the user presses Enter."""
    input(message)


def is_leap_year(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0 :
                typing(f"{year} is a Leap Year.\n")
            else:
                typing(f"{year} is not a Leap Year.\n")
        else:
            typing(f"{year} is a Leap Year.\n")
    else:
        typing(f"{year} is not a Leap Year.\n")
        