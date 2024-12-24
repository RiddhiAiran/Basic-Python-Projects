import random
from common_functions import typing, hold_screen, clear_screen, get_input

def banker_roulette():
    """Pick a Random Person to Pay the Bill."""
    clear_screen()
    typing("Welcome to the Banker Roulette!💵 \n")
    
    while True:
        participants = get_input("👤👤👤 Enter the names of participants, separated by commas: \n").strip().split(',')
        if len(participants) < 2:
            typing("At least two participants are required to play.\n")
        else:
            break
    banker = random.choice(participants)
    typing(f"\nThe banker is 👤 : {banker.strip().title()}! They will pay the bill this time. 🎉\n")
    hold_screen()

#Main Loop
def main():
    """Main Function to Run the Roulette"""
    while True:
        clear_screen()
        start = get_input("Do you want to do the Banker Roulette? (yes/no) :").lower()
        if start == 'yes':
            hold_screen()
            banker_roulette()
        else:
            typing("Goodbye! 👋 See you next time.\n")
            break

if __name__ == '__main__':
    main()
