from logo import logo
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

def auction():
    clear_screen()
    typing("Welcome to the Secret Auction!\n")
    print(logo)
    hold_screen()
    bidders = {}
    while True:
        clear_screen()
        print(logo)
        typing("What is your name?: ")
        name = input().strip().title()
        typing("What's Your Bid : $")
        bid = float(input().strip())
        bidders[name] = bid
        typing("Are there any other bidders? Type 'yes or 'no' : ")
        status = input().strip().lower()
        if status not in ['y','yes']:
            clear_screen()
            print(logo)
            for name,value in bidders.items():
                winner_bid = 0
                winner_name = ''
                if winner_bid < value:
                    winner_bid = value
                    winner_name = name
            typing(f"The winner of this auction is {winner_name} with a bid of ${winner_bid}\n")
            hold_screen()
            break
while True:
    clear_screen()
    typing("Do you want to Participate in the Secret Auction ? (y/n): ")
    participate = input().strip().lower()
    if participate not in ['y','yes']:
        typing("Good Bye! Have a Nice Day\n")
        break
    else:
        auction()