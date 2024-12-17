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

def Pizza_Order():
    """Automatic Pizza order program, this will Order Pizza of your choice, and total bill"""
    clear_screen()
    typing("🍕🍕 Welcome to the Online Pizza Order Machine!🍕 \n")
    typing("Enter your Name : ")
    name = input().upper()
    typing("🫓 What Size Pizza do you want? S, M or L?: ")
    size = input().upper()
    typing("🥫 Do you want Pepperoni on your pizza? Y or N: ")
    pepperoni = input().upper()
    typing("🧀 Do you want extra Cheese? Y or N: ")
    extra_cheese = input().upper()
    bill = 0
    if size == 'S':
        bill += 15
    elif size == 'M':
        bill += 20
    elif size == 'L':
        bill += 25
    else:
        typing("Please enter valid value!")
    if pepperoni == 'Y':
        if size == 'S':
            bill += 2
        else:
            bill += 3
    if extra_cheese == 'Y':
        bill += 1
    typing(f"💵 Your Final Bill is : ${bill}\n")
    typing("Enjoy your Pizza! 🍕🍕 ")
    hold_screen()
while True:
    clear_screen()
    typing("Do you want to Order a Pizza 🍕 ? (Y or N) : ")
    order = input().upper()
    if order == 'Y':
        Pizza_Order()
    else:
        typing("Good Bye!\n")
        break
