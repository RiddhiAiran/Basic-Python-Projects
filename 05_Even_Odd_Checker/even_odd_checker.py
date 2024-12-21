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

def even_odd():
    """Check if Number is Even or Odd"""
    clear_screen()
    typing("Welcome to the Even and Odd Number Checker !\n")
    typing("Enter your Number : ")
    num = int(input().strip())
    if num % 2 == 0:
        typing(f"{num} is an Even Number \n")
    else:
        typing(f"{num} is an Odd Number \n")
    
while True:
    clear_screen()
    typing("Do you want to Check a Number is even or Odd ? (y/n) : ")
    check = input().strip()
    if check not in ['y','yes']:
        typing('Thank you for Coming!\n')
        break
    else:
        hold_screen()
        even_odd()
        hold_screen()
    