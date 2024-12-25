from common_functions import typing, hold_screen, clear_screen, get_input
import random
import time

def flip_coin():
    """Main coin flipper logic."""
    clear_screen()
    typing("🪙 Welcome to the Coin Flipper 🪙\n")
    typing("\n🪙 Flipping a coin...\n")
    time.sleep(1.5) # adding a delay for effect
    flip = random.choice(["Heads", "Tails"])
    typing(f"\nThe result is: {flip}!\n")
    hold_screen()

#Main Loop
def main():
    """Main Function to Run the Flipper"""
    while True:
        clear_screen()
        start = get_input("Do you want to flip the coin? (yes/no) :").lower()
        if start == 'yes':
            hold_screen()
            flip_coin()
        else:
            typing("Goodbye! 👋 See you next time.\n")
            break

if __name__ == '__main__':
    main()