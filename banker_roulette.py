import os 
import time
import random

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.system == 'nt' else 'clear')

def typing(message, delay = 0.05):
    """Print a message with a typing effect."""
    for letter in message:
        print(letter, end='', flush=True)
        time.sleep(delay)

def hold_screen(message="Press Enter to continue..."):
    input(message)

def banker_roulette():
    """Pick a Random Person to Pay the Bill."""
    clear_screen()
    typing("Welcome to the Banker Roulette!\n")
    
    while True:
        typing("Enter the names of participants, separated by commas \n")
        participants = input().strip().split(',')
        
        if len(participants) < 2:
            typing("At least two participants are required to play.\n")
        else:
            break
    banker = random.choice(participants)
    typing(f"\nThe banker is: {banker.strip()}! They will pay the bill this time. 🎉\n")

banker_roulette()
