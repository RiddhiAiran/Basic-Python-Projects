import random
from common_functions import typing, hold_screen, clear_screen, get_input

def banker_roulette():
    """Pick a Random Person to Pay the Bill."""
    clear_screen()
    typing("Welcome to the Banker Roulette!💵 \n")
    
    while True:
        typing("👤👤👤 Enter the names of participants, separated by commas: \n")
        participants = input().strip().split(',')
        
        if len(participants) < 2:
            typing("At least two participants are required to play.\n")
        else:
            break
    banker = random.choice(participants)
    typing(f"\nThe banker is 👤 : {banker.strip().title()}! They will pay the bill this time. 🎉\n")

banker_roulette()
