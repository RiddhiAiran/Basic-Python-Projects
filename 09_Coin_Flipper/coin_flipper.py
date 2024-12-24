from common_functions import typing, hold_screen, clear_screen, get_input
import random
import time

def flip_coin():
    """Main coin flipper logic."""
    clear_screen()
    typing("🪙 Welcome to the Coin Flipper 🪙\n")
    hold_screen()
    typing("\n🪙 Flipping a coin...\n")
    time.sleep(1) # adding a delay for effect
    flip = random.choice(["Heads", "Tails"])
    typing(f"The result is: {flip}!\n")
    hold_screen()

#Main Loop
while True:
    clear_screen()
    typing("Do you want to flip the coin? (yes/no) :")
    start = input().lower()
    if start == 'yes':
        flip_coin()
    else:
        typing("Goodbye! 👋 See you next time.")
        break
