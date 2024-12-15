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
    # print()

def tip_calculator():
    '''Generate Total Bill Amount Each Person will Pay Including Tip'''
    clear_screen()
    typing(" 🧾 Welcome to the tip calculator! 😇\n")

    typing("\n💵 What was the total bill? $")
    bill = float(input())
    typing("\n 📝 How much tip would you like to give? 10, 12, or 15? : ")
    tip = float(input())
    typing("\n 🧑‍🧑‍🧒‍🧒 How many people to split the bill? (at least 1) : ")
    spliting = int(input())
    each = (bill + (bill*(tip/100)))/spliting
    print("-"*70)
    typing(f"\nYour Total Bill with Tip Would be : ${bill + (bill*(tip/100))}\n\nEach person should pay: ${round(each,2)}")
    print("\n")
tip_calculator()