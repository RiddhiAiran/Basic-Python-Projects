from common_functions import typing, hold_screen, clear_screen, get_input

def play_game():
    """Main game logic"""
    clear_screen()
    typing("!!!! 🏴‍☠️ Welcome to The Treasure Island !!!🏝️\n")
    Name = get_input("What is Your Name: ")
    typing(f"{Name}, 🔎 Your Mission is to find the Treasure. Best of Luck !!🍀\n")
    hold_screen()  # Pause before starting the game
    clear_screen()

    typing("You're at the cross road. Where do you want to go?\n")
    Road = get_input(" Type 👈🏻 'Left' or 👉🏻 'Right'  : ").lower()
    if Road == "left":
        hold_screen()
        clear_screen()
        typing(" 🌊 You've come to a lake. There is an island in the middle of the lake.\n")
        lake = get_input(" 🛶 Type 'wait' to wait for a boat. 🏊🏻 Type 'swim' to swim across.: ").lower()
        if lake == 'wait':
            hold_screen()
            clear_screen()
            typing("🏝️ You have arrived at the island unharmed. 🏠 There is a house with 3 doors.\n🚪 🚪 🚪 One Red, One Yellow and One Blue.\n")
            door = get_input("Which colour do you choose?: ").lower()
            if door == "yellow":
                typing("🏆 Congrats! You found the treasure 💰💰💰\n")
                hold_screen()
            elif door == "red":
                typing("🔥🔥 Burned by fire! Game Over.\n")
                hold_screen()
            elif door == "blue":
                typing("🦁🦁 Eaten by Beasts! Game Over. 💀\n")
                hold_screen()
            else:
                typing("🏴‍☠️ Game Over 🏴‍☠️")
                hold_screen()
        else:
            typing("🦈🦈 Attacked by trout, Game Over! 💀\n")
            hold_screen()
    else:
        typing("Fall into a hole, Game Over!\n")
        hold_screen()


def main():
    """ Main Function to Run the Game """
    while True:
        clear_screen()
        start_game = get_input("Do you want to play the Treasure Island game? (yes/no) : ").lower()
        if start_game == 'yes':
            hold_screen()
            play_game()
        else:
            typing("Goodbye! 👋 See you next time.\n")
            break
    
if __name__ == '__main__':
    main()
