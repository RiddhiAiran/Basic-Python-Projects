import os
import time
import random

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def typing(message, delay=0.05):
    """Print a message with a typing effect."""
    for letter in message:
        print(letter, end='', flush=True)
        time.sleep(delay)
    print()

def hold_screen(message="Press Enter to continue..."):
    """Hold the screen until the user presses Enter."""
    input(message)

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
