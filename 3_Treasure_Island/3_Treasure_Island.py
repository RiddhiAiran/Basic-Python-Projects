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
    print()

def hold_screen(message="Press Enter to continue..."):
    """Hold the screen until the user presses Enter."""
    input(message)

def play_game():
    """Main game logic."""
    clear_screen()
    typing("!!!! 🏴‍☠️ Welcome to The Treasure Island !!!🏝️\n")
    Name = input("What is Your Name: ").title()
    typing(f"{Name}, 🔎 Your Mission is to find the Treasure. Best of Luck !!🍀")
    hold_screen()  # Pause before starting the game
    clear_screen()

    typing("You're at the cross road. Where do you want to go?")
    Road = input(" Type 👈🏻 'Left' or 👉🏻 'Right'  : ").lower()
    if Road == "left":
        typing(" 🌊 You've come to a lake. There is an island in the middle of the lake.")
        lake = input(" 🛶 Type 'wait' to wait for a boat. 🏊🏻 Type 'swim' to swim across.: ").lower()
        if lake == 'wait':
            hold_screen()
            clear_screen()
            typing("🏝️ You have arrived at the island unharmed. 🏠 There is a house with 3 doors.\n🚪 🚪 🚪 One Red, One Yellow and One Blue.")
            door = input("Which colour do you choose?: ").lower()
            if door == "yellow":
                typing("🏆 Congrats! You found the treasure 💰💰💰")
                hold_screen()
            elif door == "red":
                typing("🔥🔥 Burned by fire! Game Over.")
                hold_screen()
            elif door == "blue":
                typing("🦁🦁 Eaten by Beasts! Game Over. 💀")
                hold_screen()
            else:
                typing("🏴‍☠️ Game Over 🏴‍☠️")
                hold_screen()
        else:
            typing("🦈🦈 Attacked by trout, Game Over! 💀")
            hold_screen()
    else:
        typing("Fall into a hole, Game Over!")
        hold_screen()

# Main game loop
while True:
    clear_screen()
    typing("Do you want to play the Treasure Island game? (yes/no) : ")
    start_game = input().lower()
    if start_game == 'yes':
        hold_screen()
        play_game()
        # typing("\nDo you want to play again? (yes/no) : ")
        # replay = input().lower()
        # if replay != 'yes':
        #     typing("Thanks for playing! Goodbye! 👋\n")
        #     break
    else:
        typing("Goodbye! 👋 See you next time.\n")
        break

    # Replay option after game ends
    
