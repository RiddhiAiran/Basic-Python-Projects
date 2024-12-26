import random
from common_functions import typing, hold_screen, clear_screen, get_input
import time 

def roll():
    """Returns a Random Dice Face."""
    clear_screen()
    typing("Welcome to the Dice Roller!\n")
    dice_images = [ "1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣"]
    typing("\nLet's Roll a Dice....\n")
    time.sleep(0.5)
    face = dice_images[random.randint(0,5)]
    typing(f"\nYou Got :{face}\n\n")
    hold_screen()

def main():
    while True:
        clear_screen()
        play = get_input("Do you want to Roll a Dice ? (y/n) : ").lower()
        if play == 'y':
            hold_screen()
            roll()
        else:
            typing("Good To See You!\n")
            break

if __name__ == "__main__":
    main()